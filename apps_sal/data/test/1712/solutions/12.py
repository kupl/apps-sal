n,x,y = map(int,input().split())
while n>0 :
    s = int(input())
    a = x*(s+1)//(x+y)
    b = y*(s+1)//(x+y)
    if a*y == b*x : 
        print("Both")
    elif int(a)/x<int(b)/y : 
        print("Vova")
    else : 
        print("Vanya")
    n-=1
