import sys


def input():
    return sys.stdin.readline()


def iinput():
    return int(input())


def rinput():
    return input().split()


def rlinput():
    return [int(i) for i in input().split()]


def main():
    q = [0] * 100
    (u, v) = rlinput()
    if u <= v:
        if v == 0:
            print(0)
            return 0
        if v == u:
            print(1)
            print(v)
            return 0
        if (v - u) % 2 == 1:
            print(-1)
            return 0
        fl = True
        for i in range(70):
            if v - u & 1 << i:
                q[i - 1] += 1
                if u & 1 << i - 1:
                    fl = False
        w = [u, 0]
        if fl:
            for i in range(70):
                if q[i]:
                    w[1] += 1 << i
                    w[0] += 1 << i
        else:
            w.append(0)
            for i in range(70):
                if q[i]:
                    w[1] += 1 << i
                    w[2] += 1 << i
        print(len(w))
        print(*w)
    else:
        print(-1)


for i in range(1):
    main()
