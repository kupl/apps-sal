w, h = map(int, input().split())
a = []
for i in range(h):
    a.append(list(input()))
b = []
for i in range(w):
    b.append([a[j][i] for j in range(h)])
for i in range(w):
    b[i] == b[i][::-1]
out = ''
for i in range(w):
    t = ''
    for j in range(h):
        t += b[i][j] + b[i][j]
    out += t + '\n' + t + '\n'
print(out[:-1])
