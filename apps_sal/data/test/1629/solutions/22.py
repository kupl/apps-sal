n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
m = min(a)
a = [v - m for v in a]
d = m * n
x = x - 1
# print(a)
while a[x] > 0:
    d = d + 1
    a[x] = a[x] - 1
    x = x - 1
    if x < 0:
        x = n - 1
a[x] = d
print(' '.join(map(str, a)))
