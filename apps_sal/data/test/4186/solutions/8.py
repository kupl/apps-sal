from sys import stdin
n=int(stdin.readline().strip())
s=list(map(int,stdin.readline().strip().split()))
s.sort()
ans=0
for i in range(0,n,2):
    ans+=s[i+1]-s[i]
print(ans)

