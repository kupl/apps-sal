from bisect import bisect_left,bisect_right
n=int(input())
INF=float('inf')
l=[INF]*n
a=[int(input()) for _ in range(n)]
for i in a[::-1]:
    l[bisect_right(l,i)]=i
print(bisect_left(l,INF))
