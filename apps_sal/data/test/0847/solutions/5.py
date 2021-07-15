n,x=map(int,input().split())
a=list(map(int,input().split()))
s=abs(sum(a))
print(s//x+(1 if s%x!=0 else 0))
