import bisect,collections,copy,heapq,itertools,math,numpy,string,sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
T = S()
if T=='1':
    print((10**10*2))
    return
ans = 0
X = (-N//3)*(-1)
ind_X = ('110'*(X)).find(T)
ind_X1 = ('110'*(X+1)).find(T)
if not ind_X==-1:
    ans = 10**10-(X-1)
elif not ind_X1==-1:
    ans = 10**10-(X-1)-1
print(ans)

