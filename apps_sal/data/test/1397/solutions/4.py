n, m = [int(x) for x in input().split()]
a = []
b = [0] * n
for i in range(m):
    a.append([int(x) for x in input().split()])
    b[a[i][0] - 1] += 1
    b[a[i][1] - 1] += 1
for i in range(len(b)):
    if b[i] == 0:
        print(n - 1)
        for j in range(1, n + 1):
            if j != i + 1:
                print(i + 1, j)
        break
