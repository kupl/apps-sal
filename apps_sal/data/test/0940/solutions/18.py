a, b, c = list(map(int, input().split()))
m = max(a, b, c)
s = a + b + c - m
if s > m:
    print(0)
else:
    print(m - s + 1)
