N, K = list(map(int, input().split()))
V = [int(i) for i in input().split()]
ans = 0
for M in range(K+1):
    for m in range(M+1):
        ls = []
        for i, x in enumerate(V):
            if i < m:
                ls.append(x)
        for i, x in enumerate(V[::-1]):
            if i < min(M-m, N-m):
                ls.append(x)
        ls.sort()
        s = sum(ls)
        for i, x in enumerate(ls):
            if i < K-M and x < 0:
                s -= x
        ans = max(ans, s)
print(ans)

