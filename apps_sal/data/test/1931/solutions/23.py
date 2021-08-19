from bisect import bisect_right
from sys import stdin, stdout                           #
import math                                            #
import heapq                                           #
#
t = 1                                                  #


def aint():                                            #
    return int(input().strip())                        #


def lint():                                            #
    return list(map(int, input().split()))              #


def fint():                                            #
    return list(map(int, stdin.readline().split()))     #

    #
########################################################
s = [2]
for h in range(2, 40000):
    s.append(s[-1] + 3 * h - 1)


def main():
    n = aint()
    ans = 0
    while n >= 2:
        i = bisect_right(s, n)
        # print(i,s[i],n)
        n -= s[i - 1]
        ans += 1
    print(ans)
    # solve


t = int(input())

########################################################
for i in range(t):                                     #
    #print("Case #"+str(i+1)+":",end=" ")		       #
    main()                                             #
