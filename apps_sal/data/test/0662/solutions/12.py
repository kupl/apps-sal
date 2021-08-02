q = int(input())
b = True
w = int(input())
if w == 3:
    b = False
t = set([1, 2, 3])
g = set([w, 3])
for i in range(1, q):
    w = int(input())
    if w not in g:
        b = False
    g = {w} | (t - g)
print('YES' if b else 'NO')
