n = int(input())
a = [int(x) for x in input().split()]
b = [-1 for _ in range(n)]

dp = {}
best = -1
best2 = -1

for i, x in enumerate(a):
    p, q = dp.get(x, (1, i))
    r, t = dp.get(x - 1, (0, 0))

    if r + 1 > p:
        p, q = r + 1, i
    else:
        t = i

    dp[x] = (p, q)
    b[i] = t

    if best < 0 or dp[best][0] < p:
        best = x
        best2 = i

ans = []
m = dp[best][0]

for _ in range(m):
    ans.append(best2)
    best2 = b[best2]

ans.reverse()

print(len(ans))
print(' '.join([str(x + 1) for x in ans]))

