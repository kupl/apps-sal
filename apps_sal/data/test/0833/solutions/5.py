(n, v) = map(int, input().split())
w = []
q = [v for i in range(3003)]
for i in range(n):
    w.append(list(map(int, input().split())))
w = sorted(w, reverse=True)
s = 0
for i in w:
    a = i[0]
    b = i[1]
    if q[a + 1] >= b:
        q[a + 1] -= b
        s += b
        b = 0
    else:
        b -= q[a + 1]
        s += q[a + 1]
        q[a + 1] = 0
    if q[a] >= b:
        q[a] -= b
        s += b
        b = 0
    else:
        b -= q[a]
        s += q[a]
        q[a] = 0
print(s)
