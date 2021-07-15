n, s2 = map(int, input().split())
b = {}
s = {}
b1 = set()
s1 = set()
for i in range(n):
    v = list(map(str, input().split()))
    if v[0] == 'B':
        if v[1] in b1:
            b[v[1]] += int(v[2])
        else:
            b[v[1]] = int(v[2])
            b1.add(v[1])
    if v[0] == 'S':
        if v[1] in s1:
            s[v[1]] += int(v[2])
        else:
            s[v[1]] = int(v[2])
            s1.add(v[1])
ansb = []
anss = []

for i, j in b.items():
    ansb.append((int(i), int(j)))
ansb.sort(reverse = True)

for i, j in s.items():
    anss.append((int(i), int(j)))
anss.sort()
k = len(ansb)
p = len(anss)
i = 0
j = min(s2 - 1, p - 1)
s1 = s2

while s1 > 0 and p > 0:
    print('S', anss[j][0], anss[j][1])
    j -= 1
    s1 -= 1
    p -= 1


while s2 > 0 and k > 0:
    print('B', ansb[i][0], ansb[i][1])
    k -= 1
    s2 -= 1
    i += 1
