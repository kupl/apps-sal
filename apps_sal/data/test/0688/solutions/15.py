t = int(input())
s = input()
q = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '6': 0, '7': 0, '8': 0}
for d in s:
    if d == '5':
        q['2'] += 1
    elif d == '9':
        q['6'] += 1
    else:
        q[d] += 1
p = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '6': 0, '7': 0, '8': 0}
while t != 0:
    d = str(t % 10)
    if d == '5':
        p['2'] += 1
    elif d == '9':
        p['6'] += 1
    else:
        p[d] += 1
    t //= 10
c = len(s)
for d in list(p.keys()):
    if p[d] != 0:
        c = min(c, q[d] // p[d])
print(c)

