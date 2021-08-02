s = input()
s = list(s)
c = 0
for i in range(0, len(s), 2):
    if s[i] == '0':
        c += 1
for i in range(1, len(s), 2):
    if s[i] == '1':
        c += 1
d = 0
for i in range(0, len(s), 2):
    if s[i] == '1':
        d += 1
for i in range(1, len(s), 2):
    if s[i] == '0':
        d += 1

print(min(c, d))
