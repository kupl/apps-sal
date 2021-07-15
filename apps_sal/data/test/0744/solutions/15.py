n=int(input())
s=input()
cnt1,cnt2=0,0

for i in range(n-1):
    if s[i]=='S' and s[i+1]=='F':
        cnt1+=1
    if s[i]=='F' and s[i+1]=='S':
        cnt2+=1
if cnt1>cnt2:
    print('YES')
else:
    print('NO')
