mod = 1000000007
(a, b) = list(map(int, input().split()))
n = int(input())
c = b - a
if n % 3 == 1:
    if (n - 1) / 3 % 2 == 0:
        print((mod + a) % mod)
    else:
        print((mod - a) % mod)
elif n % 3 == 2:
    if (n - 2) / 3 % 2 == 0:
        print((mod + b) % mod)
    else:
        print((mod - b) % mod)
elif (n - 3) / 3 % 2 == 0:
    print((mod + c) % mod)
else:
    print((mod - c) % mod)
