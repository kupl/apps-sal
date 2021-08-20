n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 1
l = 0
r = 0
while l < n - 1:
    if l > r:
        r = l
    while r < n - 1:
        if a[l] < a[r + 1] - 5:
            break
        r += 1
    if r - l + 1 > ans:
        ans = r - l + 1
    l += 1
print(ans)
