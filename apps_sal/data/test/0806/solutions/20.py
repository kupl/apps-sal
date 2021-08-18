m = 10**9 + 7

n, l, r = (int(x) for x in input().split())

t = r - l + 1
tm = None
if (r + 1) % 3 == l % 3:
    tm = (t // 3,) * 3
elif ((r + 1) % 3 - l % 3) % 3 == 1:
    a = [0, 0, 0]
    a[l % 3] = 1
    tm = (t // 3 + a[0], t // 3 + a[1], t // 3 + a[2])
else:
    a = [0, 0, 0]
    a[l % 3] = 1
    a[r % 3] = 1
    tm = (t // 3 + a[0], t // 3 + a[1], t // 3 + a[2])


ans0 = ans1 = ans2 = 0
ans0, ans1, ans2 = tm
ans0o, ans1o, ans2o = tm
for i in range(n - 1):
    ans0n = (ans0o * ans0 + ans2o * ans1 + ans1o * ans2) % m
    ans1n = (ans0o * ans1 + ans1o * ans0 + ans2o * ans2) % m
    ans2n = (ans0o * ans2 + ans1o * ans1 + ans2o * ans0) % m
    ans0o, ans1o, ans2o = ans0n, ans1n, ans2n

print(ans0o % m)
