a, b, k = map(int, input().split())
if a + b <= k:
    print(0, 0)
elif a <= k:
    num = k - a
    b -= num
    print(0, b)
else:
    a = a - k
    print(a, b)
