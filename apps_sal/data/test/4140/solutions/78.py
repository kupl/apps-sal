S=list(input())
l=len(S)
s=0
for i in range(l-1):
    if S[i]==S[i+1] and S[i]=='0':
        s+=1
        S[i+1]='1'
    elif S[i]==S[i+1] and S[i]=='1':
        s+=1
        S[i+1]='0'
print(s)
