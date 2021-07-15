import sys, math, bisect

def input():
    return sys.stdin.readline()[:-1]

def main():
    MOD = 10**9 + 7
    n, m = list(map(int,input().split()))
    t = pow(2,m,MOD)-1
    print(pow(t,n,MOD))

def __starting_point():
    main()

__starting_point()
