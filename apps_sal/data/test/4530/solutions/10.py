import sys
input = sys.stdin.readline
from collections import Counter

t=int(input())
for tests in range(t):
    n=int(input())
    C=Counter(list(map(int,input().split())))

    LEN=len(C)
    MAX=max(C.values())

    if MAX<LEN:
        print(MAX)
    elif MAX==LEN:
        print(MAX-1)
    else:
        print(LEN)
        

