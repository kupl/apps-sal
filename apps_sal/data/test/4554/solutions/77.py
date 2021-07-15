W, a, b = list(map(int, input().split()))
if b+W < a:
    print((a-(b+W)))
elif b > a+W:
    print((b-(a+W)))
else:
    print((0))

