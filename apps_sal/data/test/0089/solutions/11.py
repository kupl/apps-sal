n = int(input())
(l, r) = (0, n)
ans = 0
while l < r:
    ans += r - l
    l += 1
    r -= 1
print(ans)
