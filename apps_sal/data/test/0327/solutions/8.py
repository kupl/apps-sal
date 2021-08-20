(n, k) = list(map(int, input().split(' ')))
x = 1
while x < n:
    x *= 2
if x > n:
    x //= 2
if k > 1:
    print(x + x - 1)
if k == 1:
    print(n)
