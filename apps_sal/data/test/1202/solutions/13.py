team1 = [-1]
team2 = [-1]

n = int(input())

for i in range(n):
    line = input().split()
    team1.append(int(line[0]))
    team2.append(int(line[1]))

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

