(n, l, r) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0 for i in range(100005)]
for i in range(l - 1, r):
    c[a[i]] += 1
    c[b[i]] -= 1
t = True
for i in range(0, l - 1):
    if a[i] != b[i]:
        t = False
for i in range(r, n):
    if a[i] != b[i]:
        t = False
for i in c:
    if i != 0:
        t = False
if t:
    print('TRUTH')
else:
    print('LIE')
