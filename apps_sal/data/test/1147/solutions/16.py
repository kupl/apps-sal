from bisect import bisect_left as b
R=lambda:list(map(int,input().split()))
n,x,k=R()
a=sorted(R())
print(sum(b(a,l+x)-b(a,max(u,l)) for u,l in ((u,((u-1)//x+k)*x) for u in a)))

