from itertools import islice

n = int(input())
a = [0] * n
p = [0] * n
for i in range(n):
    a[i], p[i] = list(map(int, input().split()))
prev_price = p[0]
result = 0
s = a[0]
for i in range(1, n):
    if p[i] < prev_price:
        result += prev_price * s
        s = a[i]
        prev_price = p[i]
    else:
        s += a[i]
print(result + prev_price * s)
