(a, b, c, d) = list(map(int, input().split()))
if a >= d or c >= b:
    print(0)
else:
    print(min(b, d) - max(a, c))
