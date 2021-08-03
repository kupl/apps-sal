n = int(input())
a = sorted(list(map(int, input().split())))
left, r = 0, 1
ans = 0
while r < n:
    while r < n and a[r] - a[left] <= 5:
        r += 1
    ans = max(ans, r - left)
    left += 1
print(max(ans, 1))
