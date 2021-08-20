M = 10 ** 9 + 7
r = [[(j - i) * 4 % 13 for i in range(10)] for j in range(13)]
d = [1] + [0] * 12
for c in input():
    if c > '9':
        d = [sum((d[i] for i in j)) % M for j in r]
    else:
        d = [d[(j - int(c)) * 4 % 13] for j in range(13)]
print(d[5])
