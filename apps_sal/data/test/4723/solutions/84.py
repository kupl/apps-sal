s = input()
t = input()
ns = len(s)
nt = len(t)

cand = []

for i in range(ns-nt+1):
    j = 0
    temps = list(s)
    f1 = True
    while j <= nt-1:
        if temps[i+j] == '?' or temps[i+j] == t[j]:
            temps[i+j] = t[j]
        else:
            f1 = False
            break
        j += 1
    if f1:
        temps = "".join(temps)
        cand.append(temps.replace('?', 'a'))

if len(cand) == 0:
    ans = 'UNRESTORABLE'
else:
    cand.sort()
    ans = cand[0]
print(ans)

