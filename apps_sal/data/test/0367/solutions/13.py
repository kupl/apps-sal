s = input()
alphabets = [chr(x) for x in range(ord('a'), ord('z') + 1)]
a = {}

for i in alphabets:
    a[i] = 0

for c in s:
    a[c] += 1

e = None
odds = [j for j in alphabets if a[j] % 2 == 1]
k = len(odds) // 2

if len(odds) % 2 == 1:
    e = odds[k]
    odds.remove(odds[k])

for j in odds[:k]:
    a[j] += 1
for j in odds[k:]:
    a[j] -= 1

v = []
for i in alphabets:
    if a[i] % 2 == 1:
        v.append(i * (a[i] // 2))
    else:
        v.append(i * (a[i] // 2))

z = ''.join(v) + (e if e is not None else '')
v.reverse()
z += ''.join(v)
print(z)
