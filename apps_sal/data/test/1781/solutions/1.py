n, k = map(int, input().split())

ss = []

r = [0, 0, 0]

t = 0

PASSENGERS = ('x', 'P', 'S')

# - is 0
# . is 1
# P is 10
# S is 11

for i in range(n):
    s = input()
    for c in s:
        ss.append(c)
    ss.append('\n')

for i in range(len(ss)):
    if ss[i] == '.':
        rank = 0
        if i > 0 and ss[i - 1] == 'S':
            rank += 1
        if i + 1 < len(ss) and ss[i + 1] == 'S':
            rank += 1
        ss[i] = str(rank)
        r[rank] += 1

if k > r[0]:
    k -= r[0]
    if k > r[1]:
        k -= r[1]
        r[2] = k
    else:
        r[1] = k
        r[2] = 0
else:
    r[0] = k
    r[1] = 0
    r[2] = 0

i = 0
while r[0] > 0:
    while ss[i] != '0':
        i += 1
    ss[i] = 'x'
    r[0] -= 1

i = 0
while r[1] > 0:
    while ss[i] != '1':
        i += 1
    ss[i] = 'x'
    r[1] -= 1

i = 0
while r[2] > 0:
    while ss[i] != '2':
        i += 1
    ss[i] = 'x'
    r[2] -= 1

for i in range(len(ss)):
    if ss[i] in ('0', '1', '2'):
        ss[i] = '.'

for i in range(len(ss)):
    if ss[i] == 'S':
        if i > 0 and (ss[i - 1] in PASSENGERS):
            t += 1
        if i + 1 < len(ss) and (ss[i + 1] in PASSENGERS):
            t += 1

print(t)
print(''.join(ss))
