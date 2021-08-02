s = [x for x in input()]
n = len(s)
need = 4
p = {}
for i in range(n):
    if s[i] != '!':
        p[i % 4] = s[i]
c = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}
for i in range(n):
    if s[i] == '!':
        c[p[i % 4]] += 1
print(c['R'], c['B'], c['Y'], c['G'])
