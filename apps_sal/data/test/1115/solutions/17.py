from collections import defaultdict
import sys, os, math

def __starting_point():
    #n, m = list(map(int, input().split()))
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    sm = sum(arr1)
    ans = -1
    for i in range(m):
        a, b = list(map(int, input().split()))
        if a<=sm and sm<=b:
            ans = sm
        if ans == -1 and a > sm:
            ans = a
    print(ans)

__starting_point()
