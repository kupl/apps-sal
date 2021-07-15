from sys import stdin, setrecursionlimit
import bisect, collections, copy, heapq, itertools, math, string
setrecursionlimit(10**8)

INF = float("inf")
MOD = 1000000007


def input():
    return stdin.readline().strip()



def main():

    
    a, b, x, y = list(map(int, input().split()))
    ans = abs(2*b+1-2*a)//2*min(2*x, y) + x

    print(ans)














    return

def __starting_point():
    main()

__starting_point()
