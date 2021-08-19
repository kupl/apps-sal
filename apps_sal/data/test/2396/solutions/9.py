n = int(input())
ct = {}
ctx = []
for ni in range(0, n):
    st = input().strip()[1:]
    p1 = st.index('+')
    a = int(st[:p1])
    st = st[p1 + 1:]
    p2 = st.index(')')
    b = int(st[:p2])
    c = int(st[p2 + 2:])
    v = (a + b) / c
    if v in ct:
        ct[v] += 1
    else:
        ct[v] = 1
    ctx.append(v)
st = []
for cti in ctx:
    st.append(str(ct[cti]))
print(' '.join(st))
