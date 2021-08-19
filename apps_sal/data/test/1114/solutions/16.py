input()
(f, b) = [list(map(int, input().split())) for _ in range(2)]
d = {}
z = []
for i in range(len(f)):
    if f[i] in d:
        z.append(f[i])
    d[f[i]] = i + 1
ans = 2
for it in b:
    if it not in d:
        ans = 0
if ans != 0:
    if len(d) < len(f):
        for it in z:
            if it in b:
                ans = 1
                break
if ans == 2:
    print('Possible')
    print(' '.join((str(d[i]) for i in b)))
elif ans == 1:
    print('Ambiguity')
else:
    print('Impossible')
