s = input()
lns = len(s)
r = lns
for (i, (b, c)) in enumerate(zip(s, s[1:])):
    if b != c:
        r = min(r, max(i + 1, lns - i - 1))
print(r)
