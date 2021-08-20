(a, b, c, d) = list(map(int, input().split()))
if min(b, d) - max(a, c) > 0:
    print(min(b, d) - max(a, c))
else:
    print(0)
