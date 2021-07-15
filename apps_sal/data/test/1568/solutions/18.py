n, a, b, c, t = list(map(int, input().split()))
time = list(map(int, input().split()))
ans = 0
if c >= b:
    for ti in time:
        ans += a + (c - b) * (t - ti)
else:
    ans = len(time) * a
print(ans)
    

