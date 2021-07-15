a,b=list(map(int,input().split()))
result=a
while a>=b:
    result+=a//b
    a=a//b+a%b
print(result)

