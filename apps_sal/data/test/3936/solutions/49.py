from sys import stdin, setrecursionlimit
import bisect, collections, copy, heapq, itertools, math, string
setrecursionlimit(10**8)

INF = float("inf")
MOD = 1000000007


def input():
    return stdin.readline().strip()



def main():

    n = int(input())
    s1 = input()
    s2 = input()
    ans = 1

    arrange = ""
    flag = False
    for c1, c2 in zip(s1, s2):
        if c1 == c2:
            arrange += "t"
        else:
            if flag:
                flag = False
            else:
                arrange += "y"
                flag = True
    
    flag = True
    before = ""
    for c in arrange:
        if flag:
            if c == "y":
                ans *= 6
            else:
                ans *= 3
            flag = False
        else:
            md = before+c
            if md == "yy":  ans*=3
            elif md == "yt":ans*=1
            else:           ans*=2
        before = c
        ans %= MOD

    print(ans)
        

















    return

def __starting_point():
    main()

__starting_point()
