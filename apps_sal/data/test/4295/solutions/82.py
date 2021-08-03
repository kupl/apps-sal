n, k = map(int, input().split())
x1 = n % k
x2 = abs(n % k - k)
if x1 < x2:
    print(x1)
else:
    print(x2)
