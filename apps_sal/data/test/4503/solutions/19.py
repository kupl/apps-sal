h = input()
h = h.split()
n = int(h[1])
h = int(h[0])
a = input()
a = a.split()
c = int(a[0])
for b in range(n - 1):
    c = c + int(a[b + 1])
if h > c:
    print('No')
else:
    print('Yes')
