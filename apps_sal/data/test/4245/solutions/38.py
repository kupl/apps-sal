a,b=(int(x) for x in input().split())
ans=0
count=1
while count<b:
    count+=a-1
    ans+=1
print(ans,'\n')
