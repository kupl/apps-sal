import math
import sys
from sys import stdin, stdout
from collections import Counter, defaultdict, deque
input = stdin.readline
def I(): return int(input())
def li(): return list(map(int, input().split()))


def case():
    n, k = li()
    if(k > n):
        print("NO")
        return()
    if((n - k - 1) % 2):
        print("YES")
        for i in range(k - 1):
            print(1, end=" ")
        print(n + 1 - k)
        return
    if(n - 2 * k < 0):
        print("NO")
        return
    else:

        if((n - 2 * k - 2) % 2 == 0):
            print("YES")
            for i in range(k - 1):
                print(2, end=" ")
            print(n - 2 * k + 2)
        else:
            print("NO")


for _ in range(int(input())):
    case()
