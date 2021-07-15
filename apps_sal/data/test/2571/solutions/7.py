t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(0, n, 2):
        if a[i] * a[i + 1] > 0:
            b.append(-a[i + 1])
            b.append(a[i])
        elif a[i] * a[i + 1] < 0:
            b.append(abs(a[i + 1]))
            b.append(abs(a[i]))
    print(*b)
