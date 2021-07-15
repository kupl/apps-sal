def reg(s):
    s1 = ''
    for i in s:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            s1 += chr(ord(i) - ord('A') + ord('a'))
        else:
            s1 += i
    return s1

s = set()
a = int(input())
d = dict()
t = 0
repeat = []
for i in range(a):
    x, y, z = map(str, input().split())
    if reg(x) not in d:
        d[reg(x)] = t
        t += 1
    if reg(z) not in d:
        d[reg(z)] = t
        t += 1
    s.add(reg(x))
    s.add(reg(z))
    repeat.append((d[reg(x)], d[reg(z)]))
l = [[] for i in range(len(s) + 1)]
for i in repeat:
    l[i[0]].append(i[1])
    l[i[1]].append(i[0])
n = len(s)
f = [-1] * (n + 1)
q = [0] * (n + 1)
f[d['polycarp']] = 0
q[0] = d['polycarp']
h = 0
t = 1
while h < t:
    i = q[h]
    h += 1
    for j in l[i]:
        if f[j] == -1:
            f[j] = f[i] + 1
            q[t] = j
            t += 1
print(max(f) + 1)
