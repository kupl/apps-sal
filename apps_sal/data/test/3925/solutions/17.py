s = input()
n = len(s)
rec = []
pre = s[0]
prei = 0
for i in range(1, n):
    if pre != s[i]:
        pre = s[i]
        continue
    else:
        rec.append(s[prei: i])
        pre = s[i]
        prei = i

rec.append(s[prei:])

num = 0
for i in rec:
    num = max(num, len(i))

if len(rec) >= 2:
    if rec[0][0] != rec[-1][-1]:
        num = max(num, len(rec[0] + rec[-1]))

print(num)
