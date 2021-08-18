s = input()
t = input()
sset = set()
tset = set()
j = 1
alp = {}
ds = [0] * len(s)
for i in range(len(s)):
    if not s[i] in sset:
        alp[s[i]] = j
        ds[i] = j
        sset.add(s[i])
        j += 1
    else:
        ds[i] = alp[s[i]]
j = 1
alp = {}
dt = [0] * len(t)
for i in range(len(t)):
    if not t[i] in tset:
        alp[t[i]] = j
        dt[i] = j
        tset.add(t[i])
        j += 1
    else:
        dt[i] = alp[t[i]]
for i in range(len(s)):
    if ds[i] != dt[i]:
        print('No')
        return
print('Yes')
