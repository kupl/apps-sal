key = ''

ok = []
odd = []
x = list(input())
d = {}

for i in 'abcdefghijklmnopqrstuvwxyz':
    d[i] = 0

for i in x:
    d[i] += 1

for i in 'abcdefghijklmnopqrstuvwxyz':
    if d[i]%2==1:
        odd.append(i)
odd.sort()
m = len(odd)//2
for i in range(len(odd[m:])):
    d[odd[i]] += 1
    d[odd[m:][i]] -= 1
for i in 'abcdefghijklmnopqrstuvwxyz':
    if d[i] % 2 == 1:
        key = i

s = ''
for i in 'abcdefghijklmnopqrstuvwxyz':
    s += (i * (d[i]//2))

print(s+key+s[::-1])

