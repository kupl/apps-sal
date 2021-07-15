# cook your dish here

try:
    n=int(input())
    s=list(map(int,input().split()))
    e=list(map(int,input().split()))
    flag=0
    o=[]
    for i in range(len(s)):
        if (s[i]>=flag):
            o.append(i)
            flag=e[i]
    for i in o:
        print(i," ",end="")
        
except:
    pass
    

