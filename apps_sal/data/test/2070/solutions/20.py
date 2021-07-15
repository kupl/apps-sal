a = list(map(int,input().split()))
str = list(input())
dx = ord('a')
mp = [{} for i in range(26)]
sum = 0
ans = 0
for i in range(len(str)):
    d = ord(str[i])-dx
    if sum in mp[d]:
        ans += mp[d][sum]
    sum += a[d]
    if sum in mp[d]:
        mp[d][sum] += 1
    else:
        mp[d][sum] = 1
print(ans)

