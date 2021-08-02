from math import inf

n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]

ans = -inf
for bit in range(1, 1024):
    res = 0
    for j in range(n):
        c = 0
        for k in range(10):
            mask = 1 << k
            if f[j][k] and bit & mask:
                c += 1
        res += p[j][c]
    ans = max(ans, res)
print(ans)
