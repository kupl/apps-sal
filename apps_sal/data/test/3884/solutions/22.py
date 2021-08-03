n = int(input())
m = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = b[1:] + b[0:1]
c = m
d = 0
for i in range(n):
    k = n - 1 - i
    if b[k] <= 1 or a[k] <= 1:
        d = -1
    else:
        c = c * (1 + 1 / (b[k] - 1)) * (1 + 1 / (a[k] - 1))
if d == -1:
    print(d)
else:
    print(c - m)
