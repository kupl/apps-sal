'''
Created on 2020/08/30

@author: harurun
'''


def main():
    import sys
    pin = sys.stdin.readline
    pout = sys.stdout.write
    perr = sys.stderr.write

    N = int(pin())
    A = int(pin())
    B = int(pin())
    C = int(pin())
    D = int(pin())
    E = int(pin())

    t = min(A, B, C, D, E)
    if N % t == 0:
        print(N // t + 4)
    else:
        print(N // t + 5)
    return


main()
