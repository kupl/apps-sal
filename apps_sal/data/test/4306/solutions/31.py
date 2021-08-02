A, B, C, D = map(int, input().split())
if A < C and B >= D:
    res = D - C
elif A >= C and B >= D:
    res = D - A
elif A < C and B < D:
    res = B - C
else:
    res = B - A
if res <= 0:
    print(0)
else:
    print(res)
