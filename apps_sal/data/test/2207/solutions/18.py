mod = 1000000007
ii = lambda : int(input())
si = lambda : input()
dgl = lambda : list(map(int, input()))
f = lambda : map(int, input().split())
il = lambda : list(map(int, input().split()))
ls = lambda : list(input())
from itertools import groupby
n,m=f()
cnt=0
x=''
for i in range(n):
    x=si()
c=0
for i,j in groupby(x):
    c+=(i=='B')
print(c)
