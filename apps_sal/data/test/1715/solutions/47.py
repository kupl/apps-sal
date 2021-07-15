from bisect import bisect_left

a , b , q = list(map(int, input().split()))

s = [int(input()) for i in range(a)]
t = [int(input()) for i in range(b)]
s.sort()
t.sort()
s=[float('INF')*(-1)]+s+[float('INF')]
t=[float('INF')*(-1)]+t+[float('INF')]
for i in range(q):
    x = int(input())
    sp=bisect_left(s,x)-1
    tp=bisect_left(t,x)-1
    s1=s[sp]
    t1=t[tp]
    s2=s[sp+1]
    t2=t[tp+1]
    print((min(max(x-s1,x-t1),max(s2-x,t2-x),x-s1+t2-s1,x-t1+s2-t1,s2-x+s2-t1,t2-x+t2-s1)))

