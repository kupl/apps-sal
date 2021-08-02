n, r = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
i = min(n - 1, r - 1)
prev = -1
while i > prev:
    while i > prev and arr[i] == 0:
        i -= 1
    if i == prev:
        ans = -1
        break
    prev = i
    ans += 1
    if prev + r >= n:
        break
    i = min(n - 1, i + 2 * r - 1)
print(ans)
