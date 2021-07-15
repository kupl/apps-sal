a1,a2,a3,a4=list(map(int,input().split()))
s=input()
k=0
for i in range(len(s)):
    if s[i]=='1':
        k+=a1
    if s[i]=='2':
        k+=a2
    if s[i]=='3':
        k+=a3
    if s[i]=='4':
        k+=a4
print(k)

