(w, a, b) = map(int, input().split())
if b >= a:
    print(max(0, b - (a + w)))
else:
    print(max(0, a - (b + w)))
