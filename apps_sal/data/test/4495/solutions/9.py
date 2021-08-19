(a, b, c) = map(int, input().split())
if a % c == 0:
    print(b // c - a // c + 1)
else:
    print(b // c - a // c)
