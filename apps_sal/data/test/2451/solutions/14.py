n, h, a, b, k = list(map(int,input().split()))
for _ in range(k):
    x, y, w, z = list(map(int,input().split()))
    if x == w:
        print(abs(y-z))
    elif a <= min(y,z) and max(y,z) <= b:
        print(abs(y-z)+abs(x-w))
    else:
        print((min(
            abs(y-a)+abs(z-a)+abs(x-w),
            abs(y-b)+abs(z-b)+abs(x-w)
        )))

