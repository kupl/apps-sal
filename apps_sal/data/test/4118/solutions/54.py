(a, b) = (int(x) for x in input().split())
if a >= 10 or b >= 10:
    print(-1)
else:
    print(a * b)
