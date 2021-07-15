n=int(input())
l=list(map(int,input().split()))
k=max(l)
s=[]
i=0
d=0
while(i<len(l)):
    if(len(s)==0):
        s.append(l[i])
    elif(s[-1]==l[i]):
        s.pop()
    elif(s[-1]!=l[i]):
        if(s[-1]<l[i]):
            print("NO")
            d=1
            break
        s.append(l[i])
    i+=1
if(d==0):
    if(len(s)==0 or (len(s)==1 and s[0]==k)):
        print("YES")
    else:
        print("NO")

