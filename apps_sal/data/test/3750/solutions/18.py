(k, a, b) = list(map(int, input().split()))
n = a // k + b // k
if b // k == 0 and a - k * n > 0 or (a // k == 0 and b - k * n > 0) or n == 0:
    print(-1)
else:
    print(n)
