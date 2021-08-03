n, k = list(map(int, input().split()))

x = n % k
y = abs(x - k)

if x < y:
    print(x)
else:
    print(y)
