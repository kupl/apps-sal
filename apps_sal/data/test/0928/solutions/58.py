n,k = map(int,input().split())
a = list(map(int,input().split()))
left = 0
x = 0
ans = 0
for right in a:
    x += right
    while x >= k:
        x -= a[left]
        left += 1
    ans += left
print(ans)
