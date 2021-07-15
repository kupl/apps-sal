n,k = list(map(int, input().split()))
s = list(map(int,input().split()))

old = 0
current = 0
idx = 0
ans = 0
while idx < len(s):
    if(old != 0 and s[idx] // k == 0):
        ans+= 1
        old = max(s[idx] - (k-old),0)
        idx+=1
        continue
    ans += (s[idx]+old) // k
    old = (s[idx]+old) % k
    idx+=1
if(old>0):
    ans+=1
print(ans)

