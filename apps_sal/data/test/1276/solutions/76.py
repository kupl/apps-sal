N,S=int(input()),input()
r,g,b=0,0,0
for i in list(S):
    if i=='R':r+=1
    if i=='G':g+=1
    if i=='B':b+=1
ans=r*g*b
for i in range(N-2):
    for j in range(i+1,N-1):
        if j-i>N-j-1:break
        if S[i]!=S[j]and S[j]!=S[2*j-i]and S[2*j-i]!=S[i]:
            ans-=1
print(ans)
