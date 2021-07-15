Mod=1000000007
n=int(input())
p=list( map(int, input().split()) )
s=[0,2]
for i in range(2,n+1):
    s.append( ( 2*s[i-1]-s[p[i-1]-1] + 2 + Mod ) % Mod )
print(s[n])

