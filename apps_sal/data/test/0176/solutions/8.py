k, a, b = list(map(int, input().split()))

if a < 0 and b > 0:
    print(-a // k + b // k + 1)
elif a > 0 and b > 0:
    print(b // k - (a - 1) // k)
elif a < 0 and b < 0:
    print(-a // k - (-b - 1) // k)
elif a < 0 and b == 0:
    print(-a // k + 1)
elif b > 0 and a == 0:
    print(b // k + 1)
else:
    print(1)
