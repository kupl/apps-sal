S=input()
K=int(input())
a=''
n=0

if len(S)<=K:
    n=len(S)
else:
    n=K
for i in range(n):
    if S[i]=='1':
        a='1'
        continue
    else:
        a=S[i]
        break
print(a)

