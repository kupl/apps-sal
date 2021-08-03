'''
Created on 2020/09/08

@author: harurun
'''


def main():
    import sys
    pin = sys.stdin.readline
    pout = sys.stdout.write
    perr = sys.stderr.write

    N, M = map(int, pin().split())
    L, R = map(int, pin().split())
    for i in range(M - 1):
        l, r = map(int, pin().split())
        if L < l and l <= R:
            L = l
        elif R < l:
            print(0)
            return
        if L <= r and r < R:
            R = r
        elif r < L:
            print(0)
            return
    print(R - L + 1)
    return


main()
