import sys
readline = sys.stdin.readline


def solve():
    N = int(input())
    brackets_generator = (readline().strip() for _ in range(N))
    grads_positive = list()
    grads_negative = list()
    total = 0
    for brackets in brackets_generator:
        (elevation, bottom) = (0, 0)
        for bk in brackets:
            elevation += 1 if bk == '(' else -1
            bottom = min(bottom, elevation)
        if elevation >= 0:
            grads_positive.append((bottom, elevation))
        elif elevation < 0:
            grads_negative.append((bottom - elevation, -elevation))
        total += elevation
    if total != 0:
        return False
    grads_positive.sort(reverse=True)
    grads_negative.sort(reverse=True)

    def is_good(grads):
        (elevation, bottom) = (0, 0)
        for grad in grads:
            bottom = elevation + grad[0]
            if bottom < 0:
                return False
            elevation += grad[1]
        return True
    return is_good(grads_positive) and is_good(grads_negative)


def main():
    ok = solve()
    if ok:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
