n=int(input())
s=list(map(int, input().split()))
t=[0 for i in range(6001)]
for i in range(len(s)):
    t[s[i]]+=1
ans=0
for i in range(6001):
    if t[i]>1:
        ans += t[i]-1
        t[i+1]+=t[i]-1
print(ans)
