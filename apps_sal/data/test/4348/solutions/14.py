n,k=list(map(int,input().split()))
a=list(input().strip())
count=[0]*26
aaa=ord('a')
for i in a:
    count[ord(i)-aaa]+=1
deletables=-1
for i in range(26):
    if(count[i]>=k):
        count=k
        ele=i
        break
    deletables=i
    k-=count[i]
ans=""
for i in a:
    if(ord(i)-aaa<=deletables):
        continue
    if(chr(ele+aaa)==i):
        if(count>0):
            count-=1
        else:
            ans+=i
    else:
        ans+=i
print(ans)
