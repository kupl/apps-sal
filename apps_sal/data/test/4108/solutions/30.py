s = list(input())
t = list(input())

n = len(s)
ch = 0
ch1 = 0
ans = 0

d = {}
d1 = {}

st = 1
st1 = 1

s_new = []
t_new = []

for i in range(n):
    if s[i] not in d:
        d[s[i]] = st
        st += 1

for g in range(n):
    if t[g] not in d1:
        d1[t[g]] = st1
        st1 += 1

for h in range(n):
    s_new.append(d[s[h]])
    t_new.append(d1[t[h]])

if s_new == t_new:
    print('Yes')
else:
    print('No')
