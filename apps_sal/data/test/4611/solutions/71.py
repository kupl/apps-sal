'''
Created on 2020/08/31

@author: harurun
'''


def main():
    import sys
    pin = sys.stdin.readline
    pout = sys.stdout.write
    perr = sys.stderr.write

    N = int(pin())
    time = 0
    nx = 0
    ny = 0
    for i in range(N):
        t, x, y = list(map(int, pin().split()))
        d = abs(nx - x) + abs(ny - y)
        s = t - time
        if d <= s and s % 2 == d % 2:
            time = t
            nx = x
            ny = y
        else:
            print("No")
            return
    print("Yes")
    return


main()
# kaisetuAC
