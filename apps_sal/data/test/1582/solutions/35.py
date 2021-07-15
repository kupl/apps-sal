n = int(input())
num = [[0] * 10 for i in range(10)]
for i in range(1,n+1):
    j = str(i)
    x = j[0]
    y = j[-1]
    if x != '0' and y != '0':
        num[int(x)][int(y)] += 1
ans = 0
for i in range(1,10):
    for j in range(1,10):
        ans += num[i][j] * num[j][i]
print(ans)
