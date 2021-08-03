n, k = list(map(int, input().split()))

a = n % k
if (a <= int(k / 2)):
    print(a)
else:
    print((k - a))
