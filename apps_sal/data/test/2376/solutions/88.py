def main():
    N, W = list(map(int, input().split()))
    WV = [tuple(map(int, input().split())) for _ in range(N)]
    cur = {0: 0}
    for w, v in WV:
        keys = sorted(list(cur.keys()), reverse=True)
        for k in keys:
            if k + w > W:
                continue
            cur[k + w] = max(cur[k] + v, cur.get(k + w, 0))
    return max(cur.values())

print((main()))

