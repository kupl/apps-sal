a, b, c, k = list(map(int, input().split()))
if k <= a:
    print(k)
elif k <= a + b:
    print(a)
else:
    print((a-(k - a - b)))

