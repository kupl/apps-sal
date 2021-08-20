n = int(input())
a = [0]
for i in range(n):
    st = []
    t = int(input())
    for i in a:
        st.append(i + t)
        st.append(i - t)
    a = st
r = False
for i in a:
    if (i % 360 + 360) % 360 == 0:
        r = True
print('YES' if r else 'NO')
