import collections

n,k,q = map(int,input().split())
pt = [int(input()) for i in range(q)]
ans = collections.Counter(pt)

for i in range(n):
    if k-q+ans[i+1] >= 1:
        print('Yes')
    else:
        print('No')
