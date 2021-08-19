n = int(input())
a = list(map(int, input().split()))
b = [0] * (n + 1)
q = []
for i in range(1, n + 1):
    b[i] = a[i - 1]
for i in range(1, n + 1):
    c = [0] * (n + 1)
    c[i] = 1
    x = i
    while 1:
        x = b[x]
        if c[x] == 1:
            q.append(x)
            break
        else:
            c[x] = 1
print(*q)
