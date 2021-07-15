a,b=map(int,input().split())
ans=(a+b)//2
print(ans if (a+b)&1!=1 else ans+1)
