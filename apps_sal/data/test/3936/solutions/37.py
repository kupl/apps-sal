import sys
from heapq import heappush, heappop
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())

mod = 10 **9 + 7
def main():
    n = ii()
    s = []
    s.append(input())
    s.append(input())
    if s[0][0] == s[1][0]:
        ans = 3
    else:
        ans = 6

    for i in range(1,n):
        if s[0][i-1] == s[1][i-1]:
            ans  *= 2
            ans %= mod
        else:
            if s[0][i] != s[0][i-1] and s[1][i] != s[1][i-1] and s[0][i] != s[1][i]:
                ans *= 3
                ans %= mod
    print(ans)
            

            





def __starting_point():
    main()
__starting_point()
