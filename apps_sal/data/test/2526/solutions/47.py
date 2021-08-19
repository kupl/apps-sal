import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    (x, y, a, b, c) = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    p.sort(reverse=True)
    q.sort(reverse=True)
    r.sort(reverse=True)
    p = [10 ** 10] + p[:x]
    q = [10 ** 10] + q[:y]
    r += [0] * (a + b)
    ans = sum(p) + sum(q) - 2 * 10 ** 10
    (pcnt, qcnt) = (0, 0)
    for i in range(x + y):
        if p[-1 - pcnt] >= r[i] and q[-1 - qcnt] >= r[i]:
            break
        elif p[-1 - pcnt] > q[-1 - qcnt]:
            ans += -q[-1 - qcnt] + r[i]
            qcnt += 1
        else:
            ans += -p[-1 - pcnt] + r[i]
            pcnt += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
