(n, k) = map(int, input().split())
a = n % k
if abs(a) < abs(a - k):
    print(abs(a))
else:
    print(abs(a - k))
