t=int(input())
for i in range(t):
    n=int(input())
    s=str(input())
    a=len(s)
    if a%2==0:
        x=0
        for j in range(a):
            if j%2==1:
                if int(s[j])%2==0:
                    x+=1
        if x>0:
            print(2)
        else:
            print(1)
    else:
        x=0
        for j in range(a):
            if j%2==0:
                if int(s[j])%2==1:
                    x+=1
        if x>0:
            print(1)
        else:
            print(2)
