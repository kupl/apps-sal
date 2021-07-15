N=int(input());S=input();C=set("RGB");L=[{c:0for c in C}];M=L[:];z=-sum(C==set(S[j]+S[j+r]+S[j+2*r])for r in range(1,(N+1)//2)for j in range(N-2*r))
for c in S:L+=[L[-1].copy()];L[-1][c]+=1
for c in reversed(S):M+=[M[-1].copy()];M[-1][c]+=1
for c,l,m in zip(S,L,reversed(M[:-1])):a,b=C-set(c);z+=l[a]*m[b]+l[b]*m[a]
print(z)
