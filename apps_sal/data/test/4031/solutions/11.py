n = int(input())
ss = []
for i in range(n):
    x = input().strip()
    ss.append(x)
ss = sorted(ss, key=len)
ok = True
i = 0
while i < len(ss) - 1 and ok:
    if ss[i] not in ss[i + 1]:
        ok = False
    i += 1
if not ok:
    print('NO')
else:
    print('YES')
    for x in ss:
        print(x)
