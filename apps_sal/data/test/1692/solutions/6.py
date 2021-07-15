n=input()
ans=0
for i in range(len(n)-1):
    if int(n[i:i+2])%4==0:
        ans+=i+1
for i in n:
    if int(i)%4==0:
        ans+=1
print(ans)
