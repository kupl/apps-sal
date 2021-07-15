lst = [0] + [_ in "IEAOUY" for _ in input()]
n = len(lst) - 1
for _ in range(1, n + 1):
    lst[_] += lst[_ - 1]
ans = 0
s = 0
for l in range(1, n // 2 + 1):
    s += lst[n - l + 1] - lst[l - 1]
    ans += s / l + s / (n - l + 1)
if n % 2:
    s += lst[n // 2 + 1] - lst[n // 2]
    ans += s / (n // 2 + 1)
print('%0.9f' % ans)
