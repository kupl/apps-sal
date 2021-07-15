s=input()
memo1=[]
memo2=[0]
for i in range(1,len(s)):
    if s[i-1]+s[i]=='RL':
        memo1.append(i)
    if s[i-1]+s[i]=='LR':
        memo2.append(i)
memo2.append(len(s))
n=len(memo1)
ans=[0]*len(s)

for i in range(n):
    r=memo1[i]-memo2[i]
    l=memo2[i+1]-memo1[i]

    if (r+l)%2==0:
        ans[memo1[i]]=(r+l)//2
        ans[memo1[i]-1]=(r+l)//2
    else:
        temp=(r+l)//2
        if l>r:
            ans[memo1[i]]=temp+l%2
            ans[memo1[i]-1]=temp+r%2
        else:
            ans[memo1[i]-1]=temp+r%2
            ans[memo1[i]]=temp+l%2
for a in ans:
    print(a,end=' ')
