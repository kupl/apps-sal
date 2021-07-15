N=int(input())
A=list(map(int, input().split()))
s=[0]*N

for i,a in enumerate(A):
    s[i]=a-i-1
s.sort()

if N%2==0:
    b=(s[N//2-1]+s[N//2])//2
else:
    b=s[N//2]

ans=0
for i,a in enumerate(s):
    ans+=abs(a-b)
print(ans)
