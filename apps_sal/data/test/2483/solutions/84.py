(N, C) = map(int, input().split())
table = [[0] * (10 ** 5 + 1) for i in range(C)]
st = [[] for i in range(C)]
for i in range(N):
    (s, t, c) = map(int, input().split())
    st[c - 1].append([s, t])
st_new = [[] for i in range(C)]
for c in range(C):
    if st[c]:
        st[c].sort()
        st_new[c].append(st[c][0])
        n = len(st[c])
        for i in range(1, n):
            (si, ti) = st[c][i]
            (sii, tii) = st_new[c][-1]
            if si == tii:
                st_new[c][-1][1] = ti
            else:
                st_new[c].append([si, ti])
for c in range(C):
    for (s, t) in st_new[c]:
        table[c][s - 1] += 1
        table[c][t] -= 1
for c in range(C):
    for i in range(1, 10 ** 5 + 1):
        table[c][i] += table[c][i - 1]
ans = 0
for i in range(10 ** 5 + 1):
    num = 0
    for c in range(C):
        num += table[c][i]
    ans = max(ans, num)
print(ans)
