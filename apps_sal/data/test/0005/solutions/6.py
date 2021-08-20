(n, p, l, r) = map(int, input().split())
if l == 1:
    if r == n:
        print(0)
    else:
        print(abs(p - r) + 1)
elif r == n:
    print(abs(l - p) + 1)
else:
    print(min(abs(p - l), abs(p - r)) + abs(r - l) + 2)
