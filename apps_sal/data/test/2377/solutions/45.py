from math import ceil
n, h = map(int, input().split())
a = []
b = []
for i in range(n):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)
ma = max(a)
mb = [i for i in b if i > ma]
mb.sort(reverse=True)
if sum(mb) >= h:
    i = 0
    while h > 0:
        h -= mb[i]
        i += 1
    print(i)
else:
    cnt = len(mb)
    h -= sum(mb)
    print(cnt + ceil(h/ma))
