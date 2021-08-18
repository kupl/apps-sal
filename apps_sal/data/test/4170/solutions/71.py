n = int(input())
h = list(map(int, input().split()))
ans = 0
right = 0
for left in range(n):
    while right < n - 1 and h[right] >= h[right + 1]:
        right += 1
    ans = max(ans, right - left)
    if right == left:
        right += 1
print(ans)
