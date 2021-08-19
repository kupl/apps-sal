s = input()
l = len(s)
ans = l
for (i, (e1, e2)) in enumerate(zip(s, s[1:]), 1):
    if e1 != e2:
        ans = min(ans, max(i, l - i))
print(ans)
