(w, a, b) = map(int, input().split())
if len(sorted(set(range(a, a + w + 1)) & set(range(b, b + w + 1)))) != 0:
    print('0')
elif b >= a + w:
    print(b - a - w)
elif a >= b + w:
    print(a - b - w)
