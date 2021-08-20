(_, k) = map(int, input().split())
val = [0] + list(map(int, input().split()))
n = len(val)
pls = []
(cur, i, sm) = (0, 0, 0)
while i < n:
    if val[i] >= 0:
        cur += 1
    else:
        if cur > 0:
            pls.append(cur)
        cur = 0
    i += 1
sm = sum((p for p in pls))
pls = pls[1:]
if cur > 0:
    one = cur
    sm += cur
else:
    one = 10 ** 19
ans = 0
for i in range(1, n):
    if val[i] >= 0 and val[i - 1] < 0 or (val[i] < 0 and val[i - 1] >= 0):
        ans += 1
if n - sm > k:
    print(-1)
else:
    pls.sort()
    rem = k - (n - sm)
    for p in pls:
        if rem >= p:
            rem -= p
            ans -= 2
    if rem >= one:
        ans -= 1
    print(ans)
