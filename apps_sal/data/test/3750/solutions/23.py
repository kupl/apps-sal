k, a, b = list(map(int, input().split()))
if a < k and b < k:
    print(-1)
elif min(a, b) < k and max(a, b) % k:
    print(-1)
else:
    print(a // k + b // k)
