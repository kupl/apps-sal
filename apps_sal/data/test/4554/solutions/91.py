(w, a, b) = map(int, input().split())
if a < b:
    if a + w < b:
        print(b - a - w)
    else:
        print(0)
elif a > b:
    if b + w < a:
        print(a - b - w)
    else:
        print(0)
else:
    print(0)
