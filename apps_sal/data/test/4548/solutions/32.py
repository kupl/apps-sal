(a, b, c) = input().split()
a = int(a)
b = int(b)
c = int(c)
d = list(map(int, input().split()))
e = 0
f = 0
for i in range(b):
    if d[i] > c:
        e = e + 1
    if d[i] < c:
        f = f + 1
if e > f:
    print(f)
else:
    print(e)
