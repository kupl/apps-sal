(h, w) = map(int, input().split())
a = [str(input()) for _ in range(h)]
b = []
for i in range(h):
    if a[i] != '.' * w:
        b.append(a[i])
c = []
for h in range(w):
    num = 0
    for j in b:
        if j[h] == '.':
            num += 1
    if num == len(b):
        c.append(h)
for k in b:
    word = ''
    for l in range(w):
        if l not in c:
            word += k[l]
    print(word)
