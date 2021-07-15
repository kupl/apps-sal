k, a, b = map(int, input().split())
if (b > a):
    a, b = b, a
if (a // k > 0 and b // k > 0):
    print(a // k + b // k)
elif (b < k and a % k == 0):
    print(a // k)
else:
    print(-1)
