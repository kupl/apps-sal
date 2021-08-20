s = input()
f = s[0] == 'A'
cnt = 0
for i in range(2, len(s) - 1):
    if s[i] == 'C':
        cnt += 1
f = f and cnt == 1
cnt = 0
for (c, d) in zip(s, s.lower()):
    if c != d:
        cnt += 1
f = f and cnt == 2
print('AC' if f else 'WA')
