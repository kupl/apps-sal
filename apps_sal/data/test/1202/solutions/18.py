n = int(input())

team1 = [0 for i in range(n+7)]
team2 = [0 for i in range(n+7)]
for i in range(1, n+1):
    line = input().split()
    team1[i] = int(line[0])
    team2[i] = int(line[1])

for i in range(1, n+1):
    if i <= n // 2 or team1[i] < team2[n-i+1]:
        print(1, end = '')
    else:
        print(0, end = '')
print()

for i in range(1, n+1):
    if i <= n // 2 or team2[i] < team1[n-i+1]:
        print(1, end = '')
    else:
        print(0, end = '')
print()
