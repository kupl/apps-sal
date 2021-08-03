a, b, c = map(int, input().split())

if a == b:
    print(2 * c + 2 * a)
else:
    print(2 * c + min(a, b) * 2 + 1)
