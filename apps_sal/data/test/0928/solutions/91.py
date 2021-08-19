(n, k) = map(int, input().split())
a = list(map(int, input().split()))
left = 0
sum = 0
ans = 0
for right in range(n):
    sum += a[right]
    while sum >= k:
        sum -= a[left]
        left += 1
    ans += left
print(ans)
