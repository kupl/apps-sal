s = input() + '\x00'
c = 0
lp = 0
for (i, e) in enumerate(s):
    if s[lp] != e:
        if (i - lp) % 2 == 0:
            c += 1
        lp = i
print(c)
