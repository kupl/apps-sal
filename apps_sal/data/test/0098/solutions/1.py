def check(a1, b1, a2, b2, a3, b3):
    if a2 + a3 <= a1 and b2 <= b1 and (b3 <= b1):
        return True
    if b2 + b3 <= b1 and a2 <= a1 and (a3 <= a1):
        return True
    return False


def __starting_point():
    (a1, b1) = map(int, input().split())
    (a2, b2) = map(int, input().split())
    (a3, b3) = map(int, input().split())
    if check(a1, b1, a2, b2, a3, b3) or check(a1, b1, b2, a2, a3, b3) or check(a1, b1, a2, b2, b3, a3) or check(a1, b1, b2, a2, b3, a3):
        print('YES')
    else:
        print('NO')


__starting_point()
