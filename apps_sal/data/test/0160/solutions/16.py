from collections import deque
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


def SI():
    return sys.stdin.readline()[:-1]


def main():

    def ok(f):
        bb = [a % f for a in aa]
        bb.sort()
        (i, j) = (0, n - 1)
        s = t = 0
        while i <= j:
            if s > t:
                t += f - bb[j]
                j -= 1
            else:
                s += bb[i]
                i += 1
        return s <= k
    (n, k) = MI()
    aa = LI()
    s = sum(aa)
    ff = []
    for d in range(1, s + 1):
        if d ** 2 > s:
            break
        if s % d == 0:
            ff.append(d)
            ff.append(s // d)
    if ff[-1] == ff[-2]:
        ff.pop()
    ff.sort(reverse=True)
    for f in ff:
        if ok(f):
            print(f)
            break


main()
