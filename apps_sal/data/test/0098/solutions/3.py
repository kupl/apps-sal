def ok(a, b, A, B):
    return a <= A and b <= B or (a <= B and b <= A)


def __starting_point():
    (A, B) = [int(x) for x in input().split()]
    (a1, b1) = [int(x) for x in input().split()]
    (a2, b2) = [int(x) for x in input().split()]
    if ok(a1 + a2, max(b1, b2), A, B):
        print('YES')
    elif ok(a1 + b2, max(b1, a2), A, B):
        print('YES')
    elif ok(b1 + a2, max(a1, b2), A, B):
        print('YES')
    elif ok(b1 + b2, max(a1, a2), A, B):
        print('YES')
    else:
        print('NO')


__starting_point()
