input()
(p, s, ans) = (1.0, 0.0, 0.0)
for x in sorted(map(float, input().split()), reverse=True):
    if x == 1:
        ans = 1
        break
    p = p * (1 - x)
    s = s + x / (1 - x)
    ans = max(ans, p * s)
print(ans)
