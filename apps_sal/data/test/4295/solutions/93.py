n, k = list(map(int, input().split()))


x = n % k

y = abs(x - k)

if x >= y:
    print(y)
else:
    print(x)

