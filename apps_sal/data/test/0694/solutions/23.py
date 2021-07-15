s = input()
a,b= map(int,input().split())
l = len(s)
su = [0]*(l+1)
p = 1
flag =0
for i in range(l-1,0,-1):
    su[i] = (su[i+1]+int(s[i])*p)%b
    p = (p*10)%b
p = 0
for i in range(0,l-1):
    p = (p+int(s[i]))%a
    if p==0 and s[i+1]!='0' and su[i+1]==0:
        print('YES')
        print(s[:i+1])
        print(s[i+1:])
        flag =1
        break
    p= (p*10)%a
if flag==0:
    print('NO')
