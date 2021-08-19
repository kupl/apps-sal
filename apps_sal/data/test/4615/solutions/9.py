(a, b, c, d, e, f) = map(int, input().split())
ans = [-1] * 9999
ans[a * 100] = 0
ans[b * 100] = 0
fin = [a * 100, 0]
p = 0
for i in range(1, f + 1):
    if ans[i] == -1:
        continue
    if (ans[i] + c) / (i - ans[i]) <= e * 0.01:
        ans[i + c] = max(ans[i] + c, ans[i + c])
    if (ans[i] + d) / (i - ans[i]) <= e * 0.01:
        ans[i + d] = max(ans[i] + d, ans[i + d])
    ans[i + a * 100] = max(ans[i + a * 100], ans[i])
    ans[i + b * 100] = max(ans[i + b * 100], ans[i])
    if ans[i] / i > p:
        p = ans[i] / i
        fin = [i, ans[i]]
print(*fin)
