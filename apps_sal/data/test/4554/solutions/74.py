(w, a, b) = map(int, input().split())
if b <= a <= b + w or a <= b <= a + w:
    print(0)
else:
    print(min(abs(b - a - w), abs(b + w - a)))
