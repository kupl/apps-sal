n=int(input())

if(n%3==0):
    x=9
    while(n%x==0):
        x*=3
    print(n//x+1)
else:
    print(n//3+1)

