n = int(input())
g = [[-1 for _ in range(15)] for _ in range(15)]
for i in range(n):
    a = int(input())
    for j in range(a):
        (x, y) = map(int, input().split())
        g[i][x - 1] = y
ans = 0
for bit in range(1 << n):
    honests = [0] * n
    for i in range(n):
        if bit & 1 << i:
            honests[i] = 1
    flg = True
    for i in range(n):
        if honests[i]:
            for j in range(n):
                if g[i][j] == -1:
                    continue
                if g[i][j] != honests[j]:
                    flg = False
    if flg:
        ans = max(ans, honests.count(1))
print(ans)
