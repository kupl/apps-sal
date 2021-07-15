p,q,r=map(int,input().split())

sum=[10**4] * 3
sum[0]=p+q
sum[1]=p+r
sum[2]=q+r
print(min(sum))
