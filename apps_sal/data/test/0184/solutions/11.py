l, r, a = input().split()
l = int(l)
r = int(r)
a = int(a)
d = max(l, r) - min(l, r)
if a <= d:
    ans = 2 * (min(l, r) + a)
else:
    a = a - d
    ans = 2 * (max(r, l) + a // 2)
print(ans)
