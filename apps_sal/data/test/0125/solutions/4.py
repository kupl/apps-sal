(a, b, c, d) = ([], [], [], [])
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
st = False
if a[3] == 1:
    if 1 in a[:3] or b[0] or c[1] or d[2]:
        st = True
if b[3] == 1:
    if 1 in b[:3] or a[2] or c[0] or d[1]:
        st = True
if c[3] == 1:
    if 1 in c[:3] or a[1] or b[2] or d[0]:
        st = True
if d[3] == 1:
    if 1 in d[:3] or a[0] or b[1] or c[2]:
        st = True
print('YES' if st else 'NO')
