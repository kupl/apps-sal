n = int(input())
friends = [list(map(str, input().split())) for i in range(n)]
days = [[0] * 366 for i in range(2)]
for i in range(n):
    if friends[i][0] == 'M':
        for j in range(int(friends[i][1]) - 1, int(friends[i][2])):
            days[0][j] += 1
    else:
        for j in range(int(friends[i][1]) - 1, int(friends[i][2])):
            days[1][j] += 1
num = 0
for i in range(366):
    if min(days[0][i], days[1][i]) > num:
        num = min(days[0][i], days[1][i])
print(num * 2)
