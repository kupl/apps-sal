w, h, n = map(int, input().split())
l = [-1] * (w + 1)
r = [-1] * (w + 1)
t = [-1] * (h + 1)
b = [-1] * (h + 1)

l[0] = 0
b[0] = 0
t[h] = h
r[w] = w


V = [0] * (n)
H = [0] * (n)
for i in range(n):
    line, index = input().split()
    index = int(index)
    if line == "V":
        r[index] = w
        V[i] = index
    else:
        t[index] = h
        H[i] = index

left = 0
mxw = 0
for i in range(1, w + 1):
    if r[i] != -1:
        l[i] = left
        r[left] = i
        mxw = max(mxw, i - left)
        left = i

bottom = 0
mxh = 0
for i in range(1, h + 1):
    if t[i] != -1:
        b[i] = bottom
        t[bottom] = i
        mxh = max(mxh, i - bottom)
        bottom = i

ans = [0] * (n)
ans[n - 1] = mxh * mxw


for i in range(n - 1, 0, -1):
    if V[i] != 0:
        mxw = max(mxw, r[V[i]] - l[V[i]])
        r[l[V[i]]] = r[V[i]]
        l[r[V[i]]] = l[V[i]]

    else:
        mxh = max(mxh, t[H[i]] - b[H[i]])
        b[t[H[i]]] = b[H[i]]
        t[b[H[i]]] = t[H[i]]

    ans[i - 1] = mxh * mxw

for i in range(n):
    print(ans[i])
