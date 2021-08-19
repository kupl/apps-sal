(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * n
for i in range(m):
    num = a[i]
    while num <= len(b) and b[num - 1] == 0:
        b[num - 1] = a[i]
        num += 1
for i in range(len(b)):
    print(b[i], end=' ')
