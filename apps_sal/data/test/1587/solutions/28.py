n = int(input())
c = list(input())
hrcnt = 0
rcnt = 0
for i in range(len(c)):
    if c[i] == 'R':
        rcnt += 1
for i in range(len(c)):
    if i + 1 <= rcnt and c[i] == 'R':
        hrcnt += 1
wcnt = len(c) - rcnt
if rcnt == len(c) or rcnt == 0:
    ans = 0
else:
    ans = rcnt - hrcnt
print(ans)
