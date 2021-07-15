n,b,p=map(int,input().split())
ans_b=0
ans_p=n*p
while n!=1:
    kol_m=n//2
    ans_b+=kol_m*(2*b+1)
    n=n-n//2
print(ans_b,ans_p)
