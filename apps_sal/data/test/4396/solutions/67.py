n = int(input())
list_bonus = [[s for s in input().split()] for j in range(0, n)]
ans = 0.0
for i in range(0, n):
    if list_bonus[i][1] == 'JPY':
        ans += float(list_bonus[i][0])
    else:
        ans += float(list_bonus[i][0]) * 380000.0
print(ans)
