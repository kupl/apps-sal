s = input()

ok = True
ok = ok and s[0] == 'A'

cs = 0
for i in range(2, len(s)-1):
    if s[i] == 'C':
        cs += 1

ok = ok and cs == 1

for i in range(1, len(s)):
    if s[i].islower():
        continue
    if s[i] == 'C':
        continue
    ok = False

print(('AC' if ok else 'WA'))

