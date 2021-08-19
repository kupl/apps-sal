(n, l, r) = map(int, input().split())
(ans1, ans2) = (0, 0)
c = 1
for i in range(n):
    if i > n - l:
        c *= 2
    ans1 += c
c = 1
for i in range(n):
    ans2 += c
    if i < r - 1:
        c *= 2
print(ans1, ans2)
