n = int(input())
a = list(map(int, input().split()))
(left, r) = (0, 0)
ans = 0
while r < n:
    while r < n and a[r] == a[left]:
        r += 1
    t = r
    t2 = r
    while t2 < n and a[t] == a[t2]:
        t2 += 1
    ans = max(ans, min(t2 - t, r - left) * 2)
    (left, r) = (t, t2)
print(ans)
