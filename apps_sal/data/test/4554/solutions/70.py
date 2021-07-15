w, a, b = map(int, input().split())
if a <= b:
    print(b - w - a if b - w - a > 0 else 0)
else :
    print(a - w - b if a - w - b > 0 else 0)
