w, a, b = map(int, input().split())

if a + w < b:
    print(b - a - w)
elif a < b + w:
    print(0)
else:
    print(a - b - w)
