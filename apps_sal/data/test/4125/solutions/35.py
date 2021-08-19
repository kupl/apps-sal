"""
Created on 2020/08/28

@author: harurun
"""


def main():
    import math
    import sys
    pin = sys.stdin.readline
    pout = sys.stdout.write
    perr = sys.stderr.write
    (N, X) = map(int, pin().split())
    x = list(map(int, pin().split()))
    m = abs(x[0] - X)
    for i in range(1, N):
        m = math.gcd(abs(x[i] - X), m)
    print(m)
    return


main()
