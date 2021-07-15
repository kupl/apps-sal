n = int(input())
data = [input().split() for i in range(n)]
ans = 0
for i in range(n):
    ans += int(data[i][1]) - int(data[i][0]) + 1
print(ans)
