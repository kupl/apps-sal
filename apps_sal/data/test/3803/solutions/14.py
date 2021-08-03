import math
hpy, atky, defy = list(map(int, input().split()))
hpm, atkm, defm = list(map(int, input().split()))
h, a, d = list(map(int, input().split()))


ans = math.inf
for i in range(defy, 101):
    for j in range(max(atky, defm + 1), 201):
        xx = math.ceil(hpm / (j - defm)) * max(0, (atkm - i))
        hh = max(xx + 1, hpy)
        ans = min(ans, (i - defy) * d + (j - atky) * a + (hh - hpy) * h)

if ans >= math.inf:
    print(0)
else:
    print(ans)
