s=input()
t=input()
ans=100000
for i in range(len(s)-len(t)+1):
    score=0
    U=s[i:i+len(t)]
    for j in range(len(t)):
        if(U[j]!=t[j]):
            score+=1
    ans=min(ans,score)
print(ans)
