(w, a, b) = list(map(int, input().split()))
if a + w < b:
    print(b - a - w)
elif b + w < a:
    print(a - b - w)
elif a <= b <= a + w:
    print(0)
else:
    print(0)
