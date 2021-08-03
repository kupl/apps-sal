#from collection import defaultdict as dd
import sys
input = sys.stdin.readline
t = int(input())
while t:
    n = int(input())
    # n,m=map(int,input().split())
    l = list(map(int, input().split()))
    s = set(l)
    if(len(s) == 1):
        print(n)
    else:
        print(1)
    t -= 1
