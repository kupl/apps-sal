s = input()
b = int(s.split('e')[1])
s = s.split('e')[0]
a = s.split('.')[0]
d = s.split('.')[1] + '0' * 101
a += d[:b]
d = d[b:]
i = 0
while i < len(a) - 1 and a[i] == '0':
    i += 1
a = a[i:]
i = len(d) - 1
while i > 0 and d[i] == '0':
    i -= 1
d = d[:i + 1]
if d == '0':
    print(a)
else:
    print(a + '.' + d)
