n = int(input())
k = int(input())
a = int(input())
b = int(input())
x = n
c = 0
if k == 1:
    c = a * (n - 1)
else:
    while x >= k:
        y = x % k
        c += y * a
        x -= y
        c += min(b, a * (x - x // k))
        x = x // k
    c += a * (x - 1)
print(c)
