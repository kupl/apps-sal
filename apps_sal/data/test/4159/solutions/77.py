A, B, K = map(int, input().split())
d = A - K
if A+B >= K:
    if d < 0:
        print(0, B + d)
    else:
        print(d, B)
else:
    print(0, 0)
