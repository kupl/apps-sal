n = int(input())
data = [input().split() for i in range(n)]
ans = 0
for i in range(n):
    if data[i][1] == 'JPY':
        ans += int(data[i][0])
    else:
        ans += float(data[i][0]) * 380000
print(ans)
