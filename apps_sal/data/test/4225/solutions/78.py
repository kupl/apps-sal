(a, b, c, k) = map(int, input().split())
if k >= a + b:
    print(a * 2 + b - k)
elif k >= a:
    print(a)
else:
    print(k)
