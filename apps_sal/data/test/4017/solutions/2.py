n = int(input())
a = [int(e) for e in input().split()]
ans = []
sm = 0
st = dict()
for i in a:
    st[i * 2] = st.get(i * 2, 0) + 1
    sm += i
for (i, j) in enumerate(a):
    t = sm - j
    if t == 2 * j and st.get(t, 0) <= 1:
        continue
    if st.get(t, 0) > 0:
        ans.append(i + 1)
print(len(ans))
print(' '.join((str(e) for e in ans)))
