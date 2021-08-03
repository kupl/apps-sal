k, a, b = list(map(int, input().split()))

if a >= k and b >= k:
    print(a // k + b // k)
elif a >= k:
    if a % k != 0:
        print(-1)
    else:
        print(a // k)
elif b >= k:
    if b % k != 0:
        print(-1)
    else:
        print(b // k)
else:
    print(-1)
