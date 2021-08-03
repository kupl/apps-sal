h = 1
input()
p = 'x'
r = 1
t = []
for c in input().lower():
    if h != 1:
        p = next(iter(set('bgr') - {p, c}))
        t.append(p)
        h = 1
    if c != p:
        t.append(c)
    else:
        h = 2
        r += 1
    p = c
if h != 1:
    p = next(iter(set('bg') - {p}))
    t.append(p)
print(r - 1)
print(''.join(t).upper())
