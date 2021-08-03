n, m = list(map(int, input().split()))

ms = [[0, 0] for i in range(n)]
for i in range(m):
    a, b, c = list(map(int, input().split()))
    ms[a - 1][0] += c
    ms[b - 1][1] += c

sol = 0
for i in range(n):
    sol += max(ms[i][0] - ms[i][1], 0)

print(sol)
