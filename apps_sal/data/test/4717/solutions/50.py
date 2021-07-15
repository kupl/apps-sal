X,A,B=map(int,input().split())
a=abs(X-A)
b=abs(X-B)
if a<b:
    ans="A"
elif b<a:
    ans="B"
print(ans)
