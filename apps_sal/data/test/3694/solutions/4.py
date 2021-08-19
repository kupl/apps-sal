import sys
3
# -*- coding: utf-8 -*-


def rl(proc=None):
    if proc is not None:
        return proc(sys.stdin.readline())
    else:
        return sys.stdin.readline().rstrip()


def srl(proc=None):
    if proc is not None:
        return list(map(proc, rl().split()))
    else:
        return rl().split()


def main():
    rl()
    a = srl(int)
    a.sort()
    cnt = 0
    for i in range(0, len(a) - 1):
        if a[i] == a[i + 1]:
            a[i] -= 1
            cnt += 1
            break
    if a[0] < 0:
        print('cslnb')
        return

    for i in range(0, len(a) - 1):
        if a[i] == a[i + 1]:
            print('cslnb')
            return

    for i, x in enumerate(a):
        cnt += x - i

    print('sjfnb' if (cnt & 1) else 'cslnb')


def __starting_point():
    main()


__starting_point()
