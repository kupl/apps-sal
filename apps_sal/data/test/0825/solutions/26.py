from math import sqrt, floor
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    def factorization(n):
        l = []
        t = n
        for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
            if t % i == 0:
                cnt = 0
                while t % i == 0:
                    cnt += 1
                    t = t // i
                l.append([i, cnt])
        if t != 1:
            l.append([t, 1])
        if not l:
            l.append([n, 1])
        return l
    n = int(input())
    if n == 1:
        print((0))
        return
    p = factorization(n)
    r = 0
    for pe in p:
        pe1 = pe[1]
        cnt = 1
        while pe1 >= cnt:
            pe1 -= cnt
            cnt = cnt + 1
            r += 1
    print(r)


def __starting_point():
    main()


__starting_point()
