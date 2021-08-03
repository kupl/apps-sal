n, x = map(int, input().split())
data = []
for i in range(x + 1):
    data.append([])
for i in range(n):
    l, r, c = map(int, input().split())
    if r - l + 1 <= x:
        data[r - l + 1].append([l, r, c])
for i in range(x + 1):
    data[i].sort()


answer = int(20000000000)
for i in range(x + 1):
    k, b = 0, int(20000000000)
    for j in range(len(data[i])):
        while k != len(data[x - i]) and (data[i][j][0] > data[x - i][k][1]):
            b = min(b, data[x - i][k][2])
            k += 1
        answer = min(answer, b + data[i][j][2])

if answer == int(20000000000):
    print(-1)
else:
    print(answer)
