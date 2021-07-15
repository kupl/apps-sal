n,k = map(int,input().split())
a = list(map(int,input().split()))

s = [0]*n
s[0] = a[0]
for i in range(1,n):
    s[i] = s[i-1] + a[i]

ans = 0
for i in range(n):
    tmp = s[i]-a[i]
    if s[n-1]-tmp < k:
        continue
    if a[i] >= k:
        ans += n-i
        continue
    left = i-1
    right = n
    while right-left > 1:
        mid = (left+right)//2
        if s[mid]-tmp >= k:
            right = mid
        else:
            left = mid
    #print(i,right)
    ans += n-right
print(ans)
