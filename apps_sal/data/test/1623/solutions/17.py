n, l, r = list(map(int, input().split()))
ans1, ans2 = 0, 0
t = 1
for i in range(l):
    ans1 += t
    t *= 2
ans1 += n - l
t = 1
for i in range(r):
    ans2 += t
    t *= 2
ans2 += (n - r) * (t // 2)
print(ans1, ans2)
