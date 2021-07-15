"""T=int(input())
for _ in range(0,T):
    N=int(input())
    a,b=map(int,input().split())
    s=input()
    s=[int(x) for x in input().split()]
    for i in range(0,len(s)):
        a,b=map(int,input().split())"""


T=int(input())
for _ in range(0,T):
    N=int(input())
    s=[int(x) for x in input().split()]
    c0=0
    c1=0
    pos=[0]*102
    for i in range(0,len(s)):
        pos[s[i]]=1
        if(s[i]%2==0):
            c0+=1
        else:
            c1+=1
        
    if(c0%2==0):
        print('YES')
    else:
        temp='NO'
        for i in range(0,len(pos)-1):
            if(pos[i]==1 and pos[i+1]==1):
                temp='YES'
                break
        print(temp)
        
    


