import math
n, k = map(int, input().split())
if (k * (k + 1)) / 2 > n:
    print(-1)

else:
    c = int(n / ((k * (k + 1)) / 2))
    a = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if i * i == n:
            a.append(i)
        elif n % i == 0:
            a.append(i)
            a.append(n // i)

    a = sorted(a)
    s = 0
    for i in range(len(a)):
        s += 1
        if a[i] > c:
            break
    c = a[s - 2]
    for i in range(1, k):
        print(c * i, end=" ")
    print(str(int(n - c * (k * (k - 1) / 2))))
