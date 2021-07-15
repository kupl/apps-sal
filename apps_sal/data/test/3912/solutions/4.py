n = int(input())
s = input()
d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
odd = []
sum = 0
for key in d:
    if d[key] % 2 == 1:
        odd.append(key)
        d[key] -= 1
    sum += d[key]

if sum // 2 < len(odd):
    print(len(s))
    for c in s:
        print(c+' ', end='')
    return
while True:
    if len(odd) == 0 or (sum // 2) % len(odd) == 0:
        break
    sum -= 2
    if sum // 2 < len(odd):
        print(len(s))
        for c in s:
            print(c + ' ', end='')
        return
    for key in d:
        odd.append(key)
        odd.append(key)
        d[key] -= 2
        if d[key] == 0:
            d.pop(key, None)
        break
if len(odd) == 0:
    odd.append('')
even = []
for key in d:
    even += [key] * (d[key] // 2)
l = (sum // 2) // len(odd)
print(len(odd))
for i in range(len(odd)):
    s = odd[i]
    for j in range(i * l, (i + 1) * l):
        s = even[j] + s + even[j]
    print(s + ' ', end='')

