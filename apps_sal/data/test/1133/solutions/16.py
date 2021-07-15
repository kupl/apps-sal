import string
n = int(input())
d = dict()
for i in range(n):
    word = input()
    chars = set(word)
    if len(chars) < 3:
        dc = ''.join(sorted(chars))
        d[dc] = d.get(dc, 0) + len(word)
best = 0
for c1 in string.ascii_lowercase:
    for c2 in string.ascii_lowercase:
        curscore = 0
        for dc in d:
            if set(dc) <= set(c1+c2):
                curscore += d[dc]
        if curscore > best:
            best = curscore
print(best)
