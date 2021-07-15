s = input().strip()
dc = set()

for i in range(ord('0'), ord('9') + 1):
    dc.add(chr(i))

dc.add('.')

s1 = ""
for i in range(1, len(s)):
    if s[i] in dc and s[i - 1] not in dc:
        s1 += " "
    if s[i] in dc:
        s1 += s[i]

a = []
s = s1.split(' ')
rub = 0
cop = 0
for i in s:
    if i != "":
        left = "00"
        right = ""
        if len(i) >= 4 and i[-3] == '.':
            left = i[-2:]
            right = i[:-3]
        else:
            right = i
        rt = ""
        for j in right:
            if j != '.':
                rt += j
        rub += int(rt)
        cop += int(left)

rub += cop // 100
cop -= (cop // 100) * 100
anss = ""
rubs = str(rub)
cnt = 1
for i in range(len(rubs) - 1, -1, -1):
    anss += rubs[i]
    if cnt % 3 == 0:
        anss += '.'
    cnt += 1
anss = list(anss)
anss.reverse()
if anss[0] == '.':
    anss = anss[1:]
anss = ''.join(anss)
print(anss, end='')
if cop != 0:
    print('.', end='')
    if cop < 10:
        print(0, end='')
    print(cop, end='')

