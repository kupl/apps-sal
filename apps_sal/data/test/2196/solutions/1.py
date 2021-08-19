n = int(input())
I = list(map(int, input().split()))
a = []
for val in I:
    a.append(val)
la = len(a)
b = []
c = []
d = -1
for i in range(0, la):
    if i == 0 or a[i] != a[i - 1]:
        b.append(a[i])
        c.append(1)
        d = d + 1
    else:
        c[d] = c[d] + 1
d = d + 1
tot = 0
idx = 0
for i in range(0, d):
    while idx < b[i]:
        if tot < 2:
            break
        else:
            tot = int(tot / 2)
            idx = idx + 1
    if idx < b[i]:
        idx = b[i]
        tot = c[i]
    else:
        tot = tot + c[i]
while tot >= 2:
    tot = int(tot / 2)
    idx = idx + 1
idx = idx + 1
res = idx
st = []
tot = 0
idx = 0
for i in range(0, d):
    while idx < b[i]:
        if tot == 0:
            break
        elif tot == 1:
            st.append(idx)
            tot = 0
            idx = idx + 1
        else:
            if tot % 2 == 1:
                st.append(idx)
            tot = int(tot / 2)
            idx = idx + 1
    if idx < b[i]:
        idx = b[i]
        tot = c[i]
        if tot % 2 == 1:
            st.append(idx)
        tot = int(tot / 2)
        idx = idx + 1
    else:
        idx = b[i]
        tot = tot + c[i]
        if tot % 2 == 1:
            st.append(idx)
        tot = int(tot / 2)
        idx = idx + 1
while tot > 0:
    if tot % 2 == 1:
        st.append(idx)
    tot = int(tot / 2)
    idx = idx + 1
lst = len(st)
print(res - lst)
