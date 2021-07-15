n = int(input())
d = {}
ish = {'a', 'e', 'o', 'i', 'u'}


def last_g(x):
    for el in x[::-1]:
        if el in ish:
            return el


for i in range(n):
    s = input()
    count = s.count('a') + s.count('e') + s.count('o') + s.count('i') + s.count('u')
    if count in d:
        d[count].append(s)
    else:
        d[count] = [s]
firsts = []
seconds = []
for e in d:
    gd = {'a': [], 'e': [], 'o': [], 'i': [], 'u': []}
    pairs = []
    for s in d[e]:
        gd[last_g(s)].append(s)
    for b in gd:
        for i in range(0, len(gd[b])-1, 2):
            seconds.append((gd[b][i], gd[b][i+1]))
        if len(gd[b])%2 == 1:
            pairs.append(gd[b][-1])
    for i in range(0, len(pairs)-1, 2):
        firsts.append((pairs[i], pairs[i+1]))
q = len(seconds)
m = len(firsts)
if m >= q:
    print(q)
    for i in range(q):
        print(firsts[i][0] + ' ' + seconds[i][0])
        print(firsts[i][1] + ' ' + seconds[i][1])
else:
    print(m + (q - m)//2)
    for i in range(m):
        print(firsts[i][0] + ' ' + seconds[i][0])
        print(firsts[i][1] + ' ' + seconds[i][1])
    for i in range(m, q-1, 2):
        print(seconds[i][0] + ' ' + seconds[i+1][0])
        print(seconds[i][1] + ' ' + seconds[i+1][1])
