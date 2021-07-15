n=int(input())
S=str(input())
r=S.count('R')
g=S.count('G')
b=S.count('B')
cnt=r*g*b
for i in range(n):
    for a in range(1,n):
        j=i+a
        k=j+a
        if k>=n:
            break
        if S[i]!=S[j] and S[j]!=S[k] and S[k]!=S[i]:
            cnt-=1

print(cnt)
