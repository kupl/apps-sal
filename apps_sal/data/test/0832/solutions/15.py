n = int(input())
teams = []
for i in range(n):
    h, a = list(map(int, input().split()))
    teams.append([h, a])
ans = 0
for i in teams:
    for j in teams:
        if i[0] == j[1]:
            ans += 1
print(ans)
