def main():
    (N, K) = list(map(int, input().split()))
    l = []
    for _ in range(N):
        (t, d) = list(map(int, input().split()))
        l.append((t, d))
    l.sort(key=lambda x: x[1], reverse=True)
    s = set()
    e = []
    t = 0
    for i in range(K):
        t += l[i][1]
        if l[i][0] in s:
            e.append(l[i])
        else:
            s.add(l[i][0])
    rl = [t + len(s) * len(s)]
    e.reverse()
    ei = 0
    for i in range(K, N):
        if l[i][0] in s:
            continue
        if ei >= len(e):
            break
        s.add(l[i][0])
        t -= e[ei][1]
        t += l[i][1]
        ei += 1
        rl.append(t + len(s) * len(s))
    return max(rl)


print(main())
