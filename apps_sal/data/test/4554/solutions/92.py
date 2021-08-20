(w, a, b) = map(int, input().split())
if b <= a + w <= b + w or b <= a <= b + w:
    print(0)
else:
    print(min(abs(a + w - b), abs(b + w - a)))
