'''
Created on 2020/08/29

@author: harurun
'''


def main():
    import copy
    import sys
    pin = sys.stdin.readline
    pout = sys.stdout.write
    perr = sys.stderr.write

    N = int(pin())
    X = list(map(int, pin().split()))
    t = (N + 1) // 2
    Y = sorted(X)
    ans1 = Y[t - 1]
    ans2 = Y[t]
    median = ans1 + ans2
    for i in range(N):
        s = X[i]
        if s == ans1:
            print(ans2)
        elif s == ans2:
            print(ans1)
        elif 2 * s < median:
            print(ans2)
        elif 2 * s > median:
            print(ans1)
    return


main()
