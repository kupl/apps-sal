input()
a, b = [], []
for i in input():
    a.append(i)
for i in input():
    b.append(i)
l, r = 0, len(a)-1
ans = 0
while l < r:
    ji = 0
    if a[l] == b[l] or a[r] == b[r] or a[l] == b[r] or a[r] == b[l] or b[l] == b[r]:
        ji = 1

    if (a[l] == b[l] and a[r] == b[r]) or (a[l] == b[r] and a[r] == b[l]):
        ji = 2
    if b[l] == b[r] and a[r] == a[l]:
        ji = 2
    ans += 2-ji
    l += 1
    r -= 1
if l == r and a[l] != b[l]:
    ans += 1
print(ans)

