s = input()
t = input()
ar = []
br = []
for x in range(len(s)):
    if s[x] in 'aeiou':
        ar.append(1)
    else:
        ar.append(0)
for x in range(len(t)):
    if t[x] in 'aeiou':
        br.append(1)
    else:
        br.append(0)
print('Yes' if ar == br else 'No')
