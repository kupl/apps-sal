k, a, b = list(map(int, input().split()))

if (a < k and b % k) or (b < k and a % k):
    print(-1)
else:
    print(a // k + b // k)

