
def ints(): return [int(x) for x in input().split()]


def solve(arr):
    p, inside, entered = [], set(), set()
    for x in arr:
        if (x < 0 and -x not in inside) or (x > 0 and x in entered):
            return []
        elif x < 0:
            inside.remove(-x)
            if len(inside) == 0:
                p.append(2 * len(entered))
                entered = set()
        else:
            inside.add(x)
            entered.add(x)
    if inside:
        return []
    return p


def main():
    while 1:
        try:
            n, = ints()
        except EOFError:
            break
        ans = solve(ints())
        if not ans:
            print('-1')
        else:
            print(len(ans))
            print(*ans)
    return


main()
