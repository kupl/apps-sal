(n, m) = map(int, input().split())
st1 = {}
st2 = {}
for i in range(m):
    s = input().split()
    (w1, w2) = (s[0], s[1])
    st1[w1] = w2
    st2[w2] = w1
test = input().split()
for x in test:
    w1 = x
    f = False
    if w1 in st1:
        f = True
        w2 = st1[w1]
    else:
        w2 = st2[w1]
    if len(w1) < len(w2):
        print(w1, end=' ')
    elif len(w2) < len(w1):
        print(w2, end=' ')
    else:
        print(w1 if f else w2, end=' ')
