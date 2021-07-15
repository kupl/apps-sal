a = []
for _ in range(5):
    a.append(int(input()))
c = 0
d = 0
for i in range(5):
    b = a[i] % 10
    if b != 0 and abs(10 - b) > c:
        c = abs(10 - b)
        d = i
e = a.pop(d)
f = 0
for j in a:
    g = j % 10
    if g == 0:
        f += j
    else:
        f += (j // 10 + 1) * 10
f += e
print(f)
