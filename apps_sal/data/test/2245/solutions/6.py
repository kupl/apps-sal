w = int(input())
for i in range(w):
    a,b=list(map(int, input().split()))
    a+=1
    if(b%3!=0):
        if(a%3==1):
            print("Bob")
        else:
            print("Alice")
    else:
        if((a%(b+1))%3==1):
            print("Bob")
        else:
            print("Alice")

