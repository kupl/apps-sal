n = int(input())
data = []
for i in range(n):
    x, h = [int(y) for y in input().split()]
    data.append([x, h])
lastOccupied = -99999999999
answer = 0
if n == 1:
    print(1)
    return
if n == 2:
    print(2)
    return
for i in range(n - 1):
    if data[i][0] - data[i][1] > lastOccupied:
        answer += 1
        lastOccupied = data[i][0]
    elif data[i][0] + data[i][1] < data[i + 1][0]:
        lastOccupied = data[i][0] + data[i][1]
        answer += 1
    else:
        lastOccupied = data[i][0]

answer += 1
print(answer)
