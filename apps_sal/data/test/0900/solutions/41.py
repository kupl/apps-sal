r = [[(j - k) * 9 % 13 for j in range(10)] for k in range(13)]
d = [1] + [0] * 12
M = 10 ** 9 + 7
for c in input():
    if c == '?':
        d = [sum(d[j] for j in k) % M for k in r]
    else:
        d = [d[(int(c) - k) * 9 % 13] for k in range(13)]
    #print(d)
print(d[5])
