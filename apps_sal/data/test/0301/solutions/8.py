import sys
input = sys.stdin.readline

u,v=list(map(int,input().split()))
if u>v:
    print(-1)
elif (v-u)%2==1:
    print(-1)
elif u==v==0:
    print(0)
elif u==v:
    print(1)
    print(u)
else:
    A=(v-u)//2
    B=(v-u)//2
    REST=v-A-B

    for i in range(64):
        if REST & (1<<i) !=0 and A & (1<<i) ==0:
            A+=(1<<i)
            REST-=(1<<i)

    if REST==0:
        print(2)
        print(A,B)

    else:
        print(3)
        print(A,B,REST)
    
    

