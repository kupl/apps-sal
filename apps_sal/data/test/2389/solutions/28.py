n,a,b,c=map(int, input().split(' '))
# print(n,a,b,c)
left=[a,b,c]
ans=[]
prev=(-1,-1)
for i in range(0,n):
    s=input()
    # print(s)
    x = {'A':0,'B':1,'C':2}[s[0]]
    y = {'A':0,'B':1,'C':2}[s[1]]
    if left[x]==left[y]==0:
        x0,y0=prev
        if x0!=-1:
            left[x0]-=1
            left[y0]+=1
            if left[x0]==0:
                ans=[]
                break
            left[x0]-=1
            left[y0]+=1
            ans[len(ans)-1]="ABC"[y0]
        else:
            ans=[]
            break
    if left[x]>left[y]:
        x,y=y,x
    left[x]+=1
    left[y]-=1
    ans.append("ABC"[x])
    prev=(x,y)

if len(ans)==0:
    print("No")
else:
    print("Yes")
    for x in ans:
        print(x)
