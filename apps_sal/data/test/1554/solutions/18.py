n = int(input())
d={}
s=input()
s=s.split()
start =0
ans=[]
for i in range(n):
    if s[i] not in d:
        d[s[i]]=1
    else:
        ans.append([start+1,i+1])
        start=i+1
        d={}
if ans==[]:
    print(-1)
else:
    print(len(ans))
    for i in range(len(ans)):
        if i==len(ans)-1:
            print(ans[i][0],n)
        else:
            print(ans[i][0],ans[i][1])

    
    

