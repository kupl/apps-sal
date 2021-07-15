n=int(input())
l=list(map(int,input().split()))
m=l.pop(l.index(max(l)))
if m<sum(l):
    print('Yes')
else:
    print('No')

