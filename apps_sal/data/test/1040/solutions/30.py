n=int(input())
S=input()

ans=""
for s in S:
    ans+=s
    
    if ans[-3:] == "fox":
        ans=ans[0:-3]
        
print(len(ans))
