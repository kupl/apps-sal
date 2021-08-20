n = int(input())
k = int(input())
a = int(input())
b = int(input())
ost = 0
res = 0
while a * (n // k) + b + n % k * a < n * a:
    ost = ost + n % k * a
    res = res + b
    n = n // k
res = res + (n - 1) * a + ost
print(res)
