(n, d) = map(int, input().split())
data = [input().split() for i in range(n)]
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        sum = 0
        for k in range(d):
            sum += (int(data[i][k]) - int(data[j][k])) ** 2
        temp = sum ** 0.5
        if temp.is_integer() == True:
            ans += 1
print(ans)
