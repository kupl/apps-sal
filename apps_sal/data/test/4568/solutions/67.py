N=int(input())
S=input()
tmp=0
ans=0
for i in range(N):
    A=set(S[:i])
    B=set(S[i:N])
    AB=A & B
    tmp=len(AB)
    if tmp > ans:
        ans=tmp
print(ans)
            

