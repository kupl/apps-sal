import sys
import numpy as np
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


def main():
    n, x = mi()
    a = li()
    cnt = 0
    for i in range(1,n):
        if a[i-1]+a[i]>x:
            cnt += a[i-1]+a[i]-x
            a[i] = max(0, x-a[i-1])
    print(cnt)
        
def __starting_point():
    main()
__starting_point()
