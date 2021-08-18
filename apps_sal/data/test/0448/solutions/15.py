import math
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

h = max(a)
if m > h:
    print(n)
else:
    for i in range(n):
        a[i] = math.ceil((a[i] / m))
    chose = max(a)
    x = 0

    for j in range(n):
        if a[j] == chose:
            x = j + 1
    print(x)
