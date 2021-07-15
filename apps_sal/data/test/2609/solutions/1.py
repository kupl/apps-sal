import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    n = int(input())
    segs = []
    for i in range(n):
        l,r = list(map(int, input().split()))
        segs.append((l,0,i))
        segs.append((r,1,i))
    segs.sort()
    active = set()
    increase = [0 for _ in range(n)]
    seq = []
    ans = 0
    for pos, p, i in segs:
        if p == 0:
            if len(seq)>1 and seq[-2:] == [2,1]:
                increase[next(iter(active))]+=1
            active.add(i)
        else:
            active.remove(i)
            if len(active) == 0:
                ans+=1
        seq.append(len(active))
    m = max(increase)
    seq = set(seq)
    if seq == {0,1}:
        print(ans-1)
    else:
        print(ans+max(increase))

    


        

