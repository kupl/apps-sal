'''
Created on 2020/08/29

@author: harurun
'''


def main():
    import sys
    pin = sys.stdin.readline
    pout = sys.stdout.write
    perr = sys.stderr.write

    W, H, x, y = map(int, pin().split())
    ans = W * H / 2
    pout(f"{ans} ")
    if W - x == x and H - y == y:
        print(1)
    else:
        print(0)
    return


main()
