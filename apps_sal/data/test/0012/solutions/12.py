x = int(input())
s = input()
cnts = s.count('S')
cntg = s.count('G')
cnt = 0
mx2 = -55
for i in range(len(s) - 1):
    if s[i] == 'G' and s[i + 1] == 'G':
        cnt += 1
    else:
        cnt = 0
    mx2 = max(cnt, mx2)
mx2 += 1
ls = []
s += '0'
s = '0' + s
for i in range(1, len(s)):
    if s[i - 1] == 'G' and s[i] == 'S' and (s[i + 1] == 'G'):
        ls.append(i)
cnt = 0
mx = -55
for i in range(len(ls)):
    c = ls[i] - 1
    while s[c] == 'G':
        cnt += 1
        c -= 1
    c = ls[i] + 1
    while s[c] == 'G':
        cnt += 1
        c += 1
    mx = max(cnt, mx)
    cnt = 0
maxx = max(mx, mx2)
if cntg == 0:
    print(0)
elif cntg > maxx and cnts > 0:
    print(maxx + 1)
else:
    print(maxx)
