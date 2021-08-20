n = int(input())
a = list(input())
b = list(input())
(x, y) = ([0] * n, [0] * n)
ans = 0
if n % 2 == 1 and a[n // 2] != b[n // 2]:
    ans += 1
for i in range(n // 2):
    t = [a[i], a[n - i - 1], b[i], b[n - i - 1]]
    tmp = 0
    tmp1 = 0
    tmp2 = 0
    tmp3 = 0
    xx = 0
    if t[0] != t[2]:
        tmp1 += 1
    if t[1] != t[3]:
        tmp1 += 1
    (t[0], t[1]) = (t[1], t[0])
    if t[0] != t[2]:
        tmp2 += 1
    if t[1] != t[3]:
        tmp2 += 1
    if t[0] != t[1]:
        t[0] = t[1]
        xx = 1
    if t[0] != t[2]:
        tmp3 += 1
    if t[1] != t[3]:
        tmp3 += 1
    if t[0] == t[1] and t[2] == t[3]:
        ans += xx
    else:
        ans += min(tmp1, tmp2, tmp3)
print(ans)
