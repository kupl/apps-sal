n = int(input())

f = [list(map(int, input().split())) for _ in range(n)]

p = [list(map(int, input().split())) for _ in range(n)]

ans = -10**10
for i in range(1, 1 << 10):
    c = [0] * n
    for j in range(10):
        if i & (1 << j):
            for k, F in enumerate(f):
                if F[j]:
                    c[k] += 1
    profit = 0
    for j in range(n):
        profit += p[j][c[j]]
    ans = max(ans, profit)

print(ans)
