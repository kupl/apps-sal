'''
Created on 2020/08/29

@author: harurun
'''


def main():
    import sys
    pin = sys.stdin.readline
    pout = sys.stdout.write
    perr = sys.stderr.write

    A, B, N = list(map(int, pin().split()))
    x = min(B - 1, N)
    ans = int(A * x / B) - A * int(x / B)
    print(ans)
    return


main()
# 解説AC
