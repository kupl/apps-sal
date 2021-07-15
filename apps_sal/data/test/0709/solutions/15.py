n = int(input())
s = bin(n)
ans=0
n = len(s)
for i in range(n-1,1,-1):
    if s[i] == '1':
        ans+=1
print(ans)
