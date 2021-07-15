n = int(input())
ar = [(0, 0)] * 367
for i in range(n):
    p, a, b = [i for i in input().split()]
    a = int(a)
    b = int(b)
    if p == 'M':
        for j in range(a, b + 1):
            ar[j] = (ar[j][0] + 1, ar[j][1])
    else:
        for j in range(a, b + 1):
            ar[j] = (ar[j][0], ar[j][1] + 1)
m = 0
for i in range(1, 367):
    m = max(m, min(ar[i][0], ar[i][1]) * 2)
print(m)
