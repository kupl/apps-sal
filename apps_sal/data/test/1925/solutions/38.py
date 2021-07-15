# floor(a/b)=(a-(a%b))/b
# ax%b=a(x%b)%b
a,b,n=map(int,input().split())
if(n>=b-1):
    print(a*(b-1)//b)
else:
    print(a*n//b)
