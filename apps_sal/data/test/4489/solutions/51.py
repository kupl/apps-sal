N = int(input())
s = {}
for i in range(N):
    x = input()
    if x in s:
        s[x] += 1
    else:
        s[x] = 1
M = int(input())
t = {}
for i in range(M):
    x = input()
    if x in t:
        t[x] += 1
    else:
        t[x] = 1

b = list(s.keys())
r = list(t.keys())
subs = []

for i in range(len(b)):
    if b[i] in r:
        subs.append(s[b[i]]-t[b[i]])
    else:
        subs.append(s[b[i]])
print((max(0,max(subs))))

