#!/usr/bin/env python3

def II(): return int(input())
def MII(): return list(map(int, input().split()))
def LII(): return list(map(int, input().split()))


def main():
    S = input()
    S = S[::-1]
    d = ['maerd', 'remaerd', 'esare', 'resare']

    f = False
    while True:
        for di in d:
            if S.startswith(di):
                f = False
                S = S.replace(di, '', 1)

        if f:
            break
        f = True

    if len(S) == 0:
        print('YES')
    else:
        print('NO')


def __starting_point():
    main()


__starting_point()
