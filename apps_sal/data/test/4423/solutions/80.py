#import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
SPs = [LS() for _ in range(N)]

tmp = 1
for SP in SPs:
    
    SP[1] = int(SP[1])
    SP.append(tmp)
    tmp += 1

SPs = sorted(SPs, key=lambda x:(x[0],-x[1]), reverse=False)

for ans in SPs:
    print(ans[2])
