n = input()
l = len(n)
res = 1000000
for x in range(1, 2 ** l):
    g = x
    s = ''
    i = 0
    while g:
        if g % 2:
            s += n[i]
        g //= 2
        i += 1
    if s.startswith('0'):
        continue
    h = int(s)
    sq = h ** 0.5
    if sq == int(sq):
        res = min(res, l - len(s))
print(res if res != 1000000 else -1)
