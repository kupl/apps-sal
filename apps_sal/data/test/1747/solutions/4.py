import sys
(n, k) = map(int, input().split())
hash = [0] * 1000001
now = 0
a = list(map(int, input().split()))
ans = 0
l = 0
for r in range(n):
    hash[a[r]] += 1
    if hash[a[r]] == 1:
        now += 1
    while now > k:
        hash[a[l]] -= 1
        if hash[a[l]] == 0:
            now -= 1
        l += 1
    if r - l + 1 > ans:
        al = l
        ar = r
        ans = r - l + 1
print(al + 1, ar + 1)
