n, m, k = [int(a) for a in input().split()]
table = []
for i in range(n):
    table.append([int(a) for a in input().split()])

# print(table)
event = []
for i in range(k):
    event.append([int(a) for a in input().split()])
multiplier = [0] * m
subtract = [0] * n
sumRes = [0] * n
for i in range(k):
    sumRes[event[i][0] - 1] -= 1
    multiplier[event[i][1] - 1] += 1

for i in range(n):
    for j in range(m):
        sumRes[i] = sumRes[i] + multiplier[j] * table[i][j]

for x in sumRes:
    print(x, end=" ")
