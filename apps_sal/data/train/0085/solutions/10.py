t=int(input())
for you in range(t):
    s=input()
    n=len(s)
    x=int(input())
    arr=[1 for i in range(n)]
    poss=1
    for i in range(n):
        if(s[i]=='1'):
            if(i-x>=0 and arr[i-x]==0 and i+x<n and arr[i+x]==0):
                poss=0
                break
        else:
            if(i-x>=0):
                arr[i-x]=0
            if(i+x<n):
                arr[i+x]=0
    if(poss==0):
        print(-1)
        continue
    isposs=""
    for i in range(n):
        if(i-x>=0 and arr[i-x]):
            isposs=isposs+'1'
        elif(i+x<n and arr[i+x]):
            isposs=isposs+'1'
        else:
            isposs=isposs+'0'
    if(isposs==s):
        for i in arr:
            print(i,end="")
        print()
    else:
        print(-1)

