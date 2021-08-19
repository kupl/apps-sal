N = int(input())
words = [input() for i in range(N)]
abc = 'abcdefghijklmnopqrstuvwxyz'


def countf(a, b):
    c = a + b
    s = 0
    for w in words:
        if w.strip(c) is '':
            s += len(w)
    return s


m = 0
for a in abc:
    for b in abc:
        if a == b:
            continue
        m = max(countf(a, b), m)
print(m)
