(w, a, b) = map(int, input().split())
if a <= b <= a + w or a <= b + w <= a + w:
    print(0)
elif a + w < b:
    print(b - a - w)
elif b + w < a:
    print(a - b - w)
