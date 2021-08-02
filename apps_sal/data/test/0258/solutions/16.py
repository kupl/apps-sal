n = int(input())
s = input()
p1 = 0
p2 = 0
s1 = 0
s2 = 0
for i in s[:n // 2]:
    if i == '?':
        p1 += 1
    else:
        s1 += int(i)

for i in s[n // 2:]:
    if i == '?':
        p2 += 1
    else:
        s2 += int(i)
if s1 < s2:
    buf = p1
    p1 = p2
    p2 = buf
    buf = s1
    s1 = s2
    s2 = buf
if p1 > p2:
    print('Monocarp')
else:
    p = abs(p1 - p2)
    ss = abs(s1 - s2)
    if ss == (p // 2) * 9:
        print('Bicarp')
    else:
        print('Monocarp')
