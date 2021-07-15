s=input()
ans=[]
pre=""
for i in s:
    if pre!=i:
        ans.append(i)
        pre=i

print(len(ans)-1)
