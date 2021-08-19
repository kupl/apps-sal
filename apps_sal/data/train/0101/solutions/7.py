for tcase in range(int(input())):
    (a, b, c, r) = list(map(int, input().split()))
    (ca, cb) = (c - r, c + r)
    (a, b) = (min(a, b), max(a, b))
    if b <= ca:
        print(b - a)
    elif cb <= a:
        print(b - a)
    elif a <= ca <= b <= cb:
        print(ca - a)
    elif ca <= a <= cb <= b:
        print(b - cb)
    elif a <= ca <= cb <= b:
        print(ca - a + (b - cb))
    elif ca <= a <= b <= cb:
        print(0)
    else:
        print(0)
