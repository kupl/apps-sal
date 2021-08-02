a, b, k = map(int, input().split())

if k >= a + b:
    print(0, 0)
elif k >= a and k - a <= b:
    print(0, b - (k - a))
else:
    print(a - k, b)
