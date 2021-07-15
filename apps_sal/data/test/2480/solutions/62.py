n,k = list(map(int,input().split()))
a = [0]+list(map(int,input().split()))
for i in range(n):
    a[i+1] += a[i]
    a[i+1] %=k
cnt = {}
ans = 0
for i in range(n+1):
    left = i-k
    if left >=0:
        ldiff = (a[left] - left)%k
        cnt[ldiff] -= 1
    x = (a[i] - i)%k
    if x <0:x+=k
    if x not in cnt:cnt[x] = 0
    ans+= cnt[x]    
    cnt[x] +=1
print(ans)


