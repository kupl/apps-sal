n, m = map(int, input().split())
ka = [list(map(int, input().split())) for _ in range(n)]

flg = [0] * (m + 1)
for i in range(n):
    for j in range(1, ka[i][0] + 1):
        food = ka[i][j]
        flg[food] += 1

result = 0
for i in range(m + 1):
    if flg[i] == n:
        result += 1
print(result)
