def get(ch):
    if(ch=='W'):
        return 'B'
    return 'W'

n,k=list(map(int,input().split()))
s=input()

pos=[0]*(n)

for i in range(0,len(s)):

    if(s[i]==s[(i+1)%n]):
        if(s[i]=='W'):
            pos[i]=1
            pos[(i+1)%n]=1
        else:
            pos[i]=2
            pos[(i+1)%n]=2


temp=0
str1=0
itr=[]

for i in range(0,len(pos)):
    if(pos[i]>0 and temp==0):
        temp=1
        str1=i
    itr.append([10**9+7,'W'])

if(temp==1):
    for i in range(str1,str1+n):
        if(pos[(i%n)]>0):
            curr=pos[(i%n)]
            ptr=i
        else:
            itr[(i%n)][0]=i-ptr
            if(curr==1):
                itr[(i%n)][1]='W'
            else:
                itr[(i%n)][1]='B'

    for i in range(str1,str1-n,-1):
        if(pos[(i%n)]>0):
            curr=pos[(i%n)]
            ptr=i
        else:
            if(ptr-i<itr[(i%n)][0]):
                itr[(i%n)][0]=ptr-i
                if(curr==1):
                    itr[(i%n)][1]='W'
                else:
                    itr[(i%n)][1]='B'

ans=''
for i in range(0,len(s)):
    if(pos[i]>0):
        ans+=s[i]
    else:
        if(itr[i][0]<=k):
            ans+=itr[i][1]
        else:
            if(k%2==0):
                ans+=s[i]
            else:
                ans+=get(s[i])

print(ans)


    


























            
    



























            
    

