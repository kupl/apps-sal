a,b=map(int,input().split())
if a==b :
    print(0)
    return
a1,a3,a5,b1,b3,b5=0,0,0,0,0,0

while a!=0 :
    if a%2==0 : a,a1= a/2 ,a1+1
    elif a%3==0 :   a,a3= a/3 ,a3+1
    elif a%5==0 : a,a5= a/5 ,a5+1
    else :  break
while b!=0 :
    if b%2==0 :     b,b1= b/2 ,b1+1
    elif b%3==0 :   b,b3= b/3 ,b3+1
    elif b%5==0 :   b,b5= b/5 ,b5+1
    else :  break
if a!=b : print(-1)
else : print(abs(a1-b1) + abs(a3-b3) + abs(a5-b5))
