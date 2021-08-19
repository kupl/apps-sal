n = int(input())
a = [int(x) for x in input().split()]
b = [0] * (n + 1)
counter = 0
for i in range(n):
    b[i] = counter
    counter += a[i]
b[n] = counter
q = int(input())
for i in range(q):
    (x, y) = [int(x) for x in input().split()]
    z = b[y] - b[x - 1]
    print(z // 10)
