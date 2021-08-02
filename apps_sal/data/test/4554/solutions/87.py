w, a, b = map(int, input().split())
n = max(a, b) - (min(a, b) + w)
if n < 0:
    print(0)
else:
    print(n)
