h, m = list(map(int, input().split()))
cur, d, c, n = list(map(int, input().split()))
ans = (cur // n) * c
if (cur % n != 0):
    ans += c
time = h * 60 + m
if (time < 20 * 60):
    cur += d * (20 * 60 - time)
ans1 = (cur // n) * 0.8 * c
if (cur % n != 0):
    ans1 += 0.8 * c
ans = min(ans, ans1)
print("%.4f" % ans)
