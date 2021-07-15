n=int(input())
k=int(input())
x=int(input())
y=int(input())
first=min(n,k)
re=first*x
re+=max((n-first),0)*y
print(re)
