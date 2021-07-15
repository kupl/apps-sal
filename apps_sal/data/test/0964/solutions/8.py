def stripe(a, b, c):
    ans = [str(a[0])]
    ans.append('\n'.join(a[2]*a[0] for _ in range(a[1])))
    ans.append('\n'.join(b[2]*b[0] for _ in range(b[1])))
    ans.append('\n'.join(c[2]*c[0] for _ in range(c[1])))
    return '\n'.join(ans)


def tt(a):
    return (a[1], a[0], a[2])


def one_two(a, b, c):
    ans = [str(a[0])]
    ans.append('\n'.join(a[2]*a[0] for _ in range(a[1])))
    for _ in range(b[1]):
        ans.append(b[2]*b[0] + c[2]*c[0])
    return '\n'.join(ans)


def solve():
    x1, y1, x2, y2, x3, y3 = list(map(int, input().split()))
    a = (x1, y1, 'A')
    b = (x2, y2, 'B')
    c = (x3, y3, 'C')

    from itertools import permutations
    for a, b, c in permutations((a, b, c)):
        for a, b, c in ((a, b, c), (tt(a), b, c), (a, tt(b), c), (a, b, tt(c)),
                        (tt(a), tt(b), c), (tt(a), b, tt(c)), (a, tt(b), tt(c)),
                        (tt(a), tt(b), tt(c))):
            if a[0] == a[1] + b[1] + c[1]:
                return stripe(a, b, c)
            if a[0] == b[0] + c[0] and b[1] == c[1] and a[0] == a[1]+b[1]:
                return one_two(a, b, c)

    return -1

print(solve())

