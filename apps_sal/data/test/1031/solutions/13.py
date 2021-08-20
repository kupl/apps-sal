n = int(input())
a = list(map(int, input().split()))
Max = 1000
Min = 1000
sum = 0
for i in range(len(a)):
    sum += a[i]
myMap = [[' '] * 2020 for i in range(2020)]
(x, y) = (1000, 0)
for i in range(n):
    if i & 1 == 0:
        for j in range(a[i]):
            myMap[x][y] = '/'
            x -= 1
            y += 1
        x += 1
    else:
        for j in range(a[i]):
            myMap[x][y] = '\\'
            x += 1
            y += 1
        x -= 1
    Max = max(Max, x)
    Min = min(Min, x)
for i in range(Min, Max + 1):
    print(''.join(myMap[i][:y]))
