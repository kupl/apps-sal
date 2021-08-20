(w, h) = map(int, input().split())
s = []
for i in range(h):
    s.append(input())
a = []
for i in range(w):
    a.append([0] * h)
for i in range(h):
    for j in range(w):
        a[j][i] = s[i][j]
for i in range(w):
    st = ''
    for c in a[i]:
        st += c * 2
    print(st)
    print(st)
