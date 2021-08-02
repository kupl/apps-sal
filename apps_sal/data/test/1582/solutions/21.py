n = int(input())
l = [[0] * 10 for i in range(10)]
for i in range(1, n + 1):
    st = str(i)
    start = int(st[0])
    end = int(st[-1])
    l[start][end] += 1
ans = 0
for i in range(10):
    for j in range(10):
        ans += l[i][j] * l[j][i]
print(ans)
