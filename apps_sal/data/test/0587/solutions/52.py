def main():
    N, K = list(map(int, input().split()))
    TD = [tuple(map(int, input().split())) for _ in range(N)]
    TD.sort(key=lambda x: x[1], reverse=True)
    s = set()
    rep = []
    for t, d in TD[:K]:
        if t in s:
            rep.append(d)
        else:
            s.add(t)
    m = sum(d for _, d in TD[:K])
    p = len(s) ** 2 + m
    for t, d in TD[K:]:
        if not rep:
            break
        if t in s:
            continue
        m += d - rep.pop()
        s.add(t)
        p = max(p, len(s) ** 2 + m)
    return p


print((main()))
