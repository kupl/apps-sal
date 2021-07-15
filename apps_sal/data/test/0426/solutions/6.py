n,k=map(int,input().split())
s=input()
if n==1 and k>=1:
    print("0")
    quit()
for i in range(n):
    if i==0:
        if s[0]=='1':
            print(s[0],end="")
            continue
        elif k>0:
            print(1,end="")
            k-=1
        else:
            print(s[i],end="")
    else:
        if s[i]=='0':
            print(0,end="")
            continue
        elif k>0:
            print(0,end="")
            k-=1
        else:
            print(s[i],end="")

