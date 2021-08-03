n = int(input())
a = list(map(int, input().split()))
m = int(input())
kill = []
for i in range(m):
    kill.append(list(map(int, input().split())))
if n == 1 and m == 1:
    print(0)
elif m == 0:
    for i in range(n):
        print(a[i])
else:
    for i in range(m):
        index = kill[i][0] - 1
        killed = kill[i][1]
        if index == 0:
            a[index + 1] += a[index] - killed
            a[index] = 0

        elif index == n - 1:
            a[index - 1] += killed - 1
            a[index] = 0
        else:
            a[index - 1] += killed - 1
            a[index + 1] += a[index] - killed
            a[index] = 0

    for i in range(n):
        print(a[i])
