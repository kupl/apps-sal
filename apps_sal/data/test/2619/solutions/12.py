import math,sys,bisect,heapq
from collections import defaultdict,Counter,deque
from itertools import groupby,accumulate
#sys.setrecursionlimit(200000000)
int1 = lambda x: int(x) - 1
#input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
ilele = lambda: map(int,input().split())
alele = lambda: list(map(int, input().split()))
ilelec = lambda: map(int1,input().split())
alelec = lambda: list(map(int1, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
#MOD = 1000000000 + 7
def Y(c):  print(["NO","YES"][c])
def y(c):  print(["no","yes"][c])
def Yy(c):  print(["No","Yes"][c])
    
dp = {}

def fun(A):
    B = list2d(101,101,0)
    for j in range(101):
        B[0][j] = A[0][j]
    for i in range(1,101):
        for j in range(101):
            B[i][j] = A[i][j] + B[i-1][j]
    for i in range(101):
        for j in range(1,101):
            B[i][j] = B[i][j] + B[i][j-1]
    return B

n,q,c = ilele()
G = defaultdict(list)
for i in range(n):
    a,b,s = ilele()
    G[(a,b)].append(s)
#print(G)
for i in range(c+1):
    #print(i,c)
    A = list2d(101,101,0)
    for j in range(1,101):
        for k in range(1,101):
            x  = G.get((j,k),[])
            for l in x:
                r = (l + i)%(c+1)
                #print(j,k,r,l,i)
                A[j][k] += r
    B = fun(A)
    dp[i] = B

for i in range(q):
    t,x1,y1,x2,y2 = ilele()
    t %= (c+1)
    #print(dp[t][x2][y2],dp[t][x2][y1])
    ans = dp[t][x2][y2]
    ans -= dp[t][x2][y1-1]
    ans -= dp[t][x1-1][y2]
    ans += dp[t][x1-1][y1-1]
    print(ans)
