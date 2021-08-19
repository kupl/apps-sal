n = int(input())
(a0, b0) = (0, 0)
ans = 1
for i in range(n):
    (a, b) = map(int, input().split())
    ans += max(min(a, b) - max(a0, b0), 0)
    if min(a, b) - max(a0, b0) >= 0 and a0 != b0:
        ans += 1
    (a0, b0) = (a, b)
print(ans)
