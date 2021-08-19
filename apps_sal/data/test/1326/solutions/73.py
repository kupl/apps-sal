"""
Created on 2020/08/23

@author: harurun
"""


def main():
    import sys
    pin = sys.stdin.readline
    pout = sys.stdout.write
    perr = sys.stderr.write
    N = int(pin())
    ans = 0
    for i in range(1, N + 1):
        ans += N // i * (N // i + 1) * i // 2
    print(ans)
    return


main()
