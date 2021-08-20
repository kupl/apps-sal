def d(q, d):
    c = 0
    while q % d == 0:
        q //= d
        c += 1
        pass
    return (c, q)
    pass


def main():
    a2 = 0
    a3 = 0
    a5 = 0
    b2 = 0
    b3 = 0
    b5 = 0
    (a, b) = map(int, input().split(' '))
    if a == b:
        print(0)
        return
        pass
    (at, bt) = (a, b)
    (a2, a) = d(a, 2)
    (a3, a) = d(a, 3)
    (a5, a) = d(a, 5)
    (b2, b) = d(b, 2)
    (b3, b) = d(b, 3)
    (b5, b) = d(b, 5)
    if a != b:
        print(-1)
        return
        pass
    print(abs(a2 - b2) + abs(a3 - b3) + abs(a5 - b5))
    pass


main()
