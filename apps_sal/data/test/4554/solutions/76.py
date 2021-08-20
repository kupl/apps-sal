(w, a, b) = map(int, input().split())
if a <= b <= a + w or b <= a <= b + w:
    print('0')
elif a + w < b:
    print(b - (a + w))
else:
    print(a - (b + w))
