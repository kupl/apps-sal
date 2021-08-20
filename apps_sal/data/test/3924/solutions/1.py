from math import ceil
(n, k) = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
last = 0
bags = 0
for i in range(n + 1):
    if i == n:
        last += a[i]
        bags += ceil(last / k)
    else:
        b = ceil(last / k)
        bags += b
        l = b * k - last
        last = a[i] - min(a[i], l)
print(bags)
