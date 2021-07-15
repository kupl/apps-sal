n,m=sorted(map(int,input().split()))
print(n*m-{1:min(m%6,6-m%6),2:2*(m in [3,7])+4*(m==2)}.get(n,n&1*m&1))

