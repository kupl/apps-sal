q = int(input())
for _ in range(q):
    n = int(input())
    Q = list(map(int, input().split()))
    res = [1] * n
    for i in range(n):
        if res[i] == 1:
            t = Q[i]
            tl = [t]
            while t != i + 1:
                t = Q[t - 1]
                tl.append(t)
                res[i] += 1
            for k in tl:
                res[k - 1] = res[i]
    print(*res)
