
n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

ans = 0

for i in range(n):
    if l[i][1] == "JPY":
        ans += int(l[i][0])
    else:
        ans += float(l[i][0]) * 380000.0
print(ans)
