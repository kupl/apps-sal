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


def main():
    n = aint()
    l = lint()
    l.sort()
    l = l[::-1]
    print(*l)


t = int(input())

########################################################
for i in range(t):                                     #
    main()                                             #
