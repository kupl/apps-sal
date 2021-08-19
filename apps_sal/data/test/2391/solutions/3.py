import sys
sys.setrecursionlimit(10 ** 6)


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def ZAlgorithm(aa):
    target = aa
    len_t = len(target)
    lcp = [-1] * len_t
    top = 1
    left = 0
    right = 0
    lcp[0] = 0
    while top < len_t:
        while top + right < len_t and target[right] == target[top + right]:
            right += 1
        lcp[top] = right
        left = 1
        if right == 0:
            top += 1
            continue
        while left + lcp[left] < right and left < right:
            lcp[top + left] = lcp[left]
            left += 1
        top += left
        right -= left
        left = 0
    return lcp


def main():
    inf = pow(2, 31)
    n = II()
    aa = LI()
    bb = LI()
    ax = [aa[i - 1] ^ aa[i] for i in range(n)]
    bx = [bb[i - 1] ^ bb[i] for i in range(n)]
    ll = ZAlgorithm(bx + [inf] + ax + ax[:-1])
    for (shift, lcp) in enumerate(ll[n + 1:]):
        if lcp == n:
            print(shift, aa[shift] ^ bb[0])


main()
