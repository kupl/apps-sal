(n, a) = list(map(int, input().split()))
arr = list(map(int, input().split()))
a -= 1
l = a
r = a
ans = 0
while l >= 0 or r < n:
    if l < 0:
        if arr[r]:
            ans += 1
    elif r >= n:
        if arr[l]:
            ans += 1
    elif l == r and arr[l] == 1:
        ans += 1
    elif arr[l] == 1 and arr[r] == 1:
        ans += 2
    l -= 1
    r += 1
print(ans)
