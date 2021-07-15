from collections import Counter
import math
import statistics
import itertools
# H,W,K=map(int,input().split())
#b=int(input())
# c=[]
# for i in a:
#     c.append(int(i))
# f = list(map(int,input().split()))
#g = [list(map(lambda x: '{}'.format(x), list(input()))) for _ in range(a)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
#two = [list(input()) for _ in range(H)]#nizigen
# lis=[]
# for i in range(Q):
#     lis.append(list(map(int,input().split())))
# a=list(map(int,input().split()))
N,M = list(map(int,input().split()))
par = [i for i in range(1,N+1)]
rank=[0]*N
# rank = [0]*(N)
def find(x):
    if par[x-1] == x:#自分が親であるかどうか
        return x
    else:
        par[x-1] = find(par[x-1]) #経路圧縮
        return par[x-1]
def same(x,y):
    return find(x) == find(y)
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if rank[x-1] < rank[y-1]:
        par[x-1] = y
    else:
        par[y-1] = x
        if rank[x-1]==rank[y-1]:rank[x-1]+=1

for i in range(M):
    a,b = list(map(int,input().split()))
    unite(a,b)

cnt=[0]*N
for i in range(N):
    cnt[find(i)-1]+=1
print((max(cnt)))


