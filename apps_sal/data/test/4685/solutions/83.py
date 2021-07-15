a,b,c=list(map(int,input().split()))
k=int(input())
print((a+b+c-max(a,b,c)+max(a,b,c)*pow(2,k)))

