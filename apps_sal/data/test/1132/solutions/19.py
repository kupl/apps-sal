mod = 1000000007
ii = lambda : int(input())
si = lambda : input()
dgl = lambda : list(map(int, input()))
f = lambda : map(int, input().split())
il = lambda : list(map(int, input().split()))
ls = lambda : list(input())
n,m=f()
l=[0]*n
for _ in range(m):
    a,b=f()
    l[a-1]+=1
    l[b-1]+=1
l.sort()
if l[0]==1 and l[1]==1 and all(i==2 for i in l[2:]):
    print('bus topology')
elif all(i==2 for i in l):
    print('ring topology')
elif all(i==1 for i in l[:n-1]) and l[-1]==n-1:
    print('star topology')
else:
    print('unknown topology')
