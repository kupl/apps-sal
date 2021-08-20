(w, a, b) = (int(T) for T in input().split())
if a + w < b:
    print(b - (a + w))
elif a <= b <= a + w:
    print(0)
else:
    print(a - (b + w))
