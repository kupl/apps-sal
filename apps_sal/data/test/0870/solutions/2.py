(d, l, v1, v2) = list(map(int, input().split()))
l -= d
if l <= 0:
    print(0.0)
else:
    print(l / (v1 + v2))
