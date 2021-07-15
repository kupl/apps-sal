S=input()
K=int(input())
S=list(S)

for j in range(len(S)):
    if S[j]=='1':
        if j==K-1:
            ans=1
            break
    else:
        x=[i for i in S if i!='1']
        ans=x[0]
        break

print(ans)

