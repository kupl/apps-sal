n,m=map(int,input().split())
s=input()
t=input()
k=-1
for i in range(n):
    if s[i]=='*':
        k=i
        break
if s[0:i]==t[0:i] and s[i+1:n]==t[m-n+i+1:m]:
    if (k==-1 and s!=t) or (n>m+1):
        print('NO')
    else:
        print('YES')
else:
    print('NO')
