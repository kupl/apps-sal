N=input()

S=N[::-1]
ans=0
for i in range(len(N)):
    if N[i]==S[i]:
        ans+=1

if ans==len(N):
    print("Yes")
else:
    print("No")

