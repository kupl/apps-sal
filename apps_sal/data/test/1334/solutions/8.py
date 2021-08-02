q, w = map(int, input().split())
s = input()
d = [i for i in s]
d = list(set(d))
d.sort()
if w > q:
    ans = s + d[0] * (w - q)
else:
    if w < q:
        s = s[:w]
    i = w - 1
    while s[i] == d[-1]:
        i -= 1
    ans = s[:i]
    ans += d[d.index(s[i]) + 1]
    ans += d[0] * (w - 1 - i)
print(ans)
