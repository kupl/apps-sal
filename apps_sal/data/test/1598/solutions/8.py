v, t = 0, ''
for c in input()[::-1]:
    if c < '1' or v:
        t += c; v += 1 - (c < '1') * 2
    else: t += '0'
print(t[::-1])
