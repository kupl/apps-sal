n=int(input())
m=10**9+7
s=bin(n)[2:]
t=[[0,0,0]for i in range(len(s)+1)]
t[0][0]=1
for i in range(1,len(s)+1):
    if s[i-1]=="0":
        t[i][0]=t[i-1][0]+t[i-1][1]
        t[i][1]=t[i-1][1]
        t[i][2]=t[i-1][1]+t[i-1][2]*3
    else:
        t[i][0]=t[i-1][0]
        t[i][1]=t[i-1][0]+t[i-1][1]
        t[i][2]=t[i-1][2]*3+t[i-1][1]*2
    for j in range(3):
        t[i][j]%=m
print(sum(t[-1])%m)
