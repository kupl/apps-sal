(w, a, b) = list(map(int, input().split()))
if a < b:
    print(b - a - w if b - a - w > 0 else 0)
else:
    print(a - b - w if a - b - w > 0 else 0)
