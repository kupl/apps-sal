# coding: utf-8
import sys
from heapq import heappush, heappop, heapify
sys.setrecursionlimit(int(1e7))

def main():
    n = int(input().strip())
    a = [int(x) for x in input().split()]
    a = [-x-1 if x>=0 else x for x in a]
    if n%2==1:
        _, i = min((x,i) for i,x in enumerate(a))
        a[i] = -a[i]-1
    print(*a)
    return

while 1:
    try: main()
    except EOFError: break
