n, l, r = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
f = True
for i in range(l - 1):
    if a[i] != b[i]:
        f = False
for i in range(r, n):
    if a[i] != b[i]:
        f = False
a1 = []
b1 = []
for i in range(l - 1, r):
    b1.append(b[i])
    a1.append(a[i])
a1.sort()
b1.sort()
for i in range(len(a1)):
    if a1[i] != b1[i]:
        f = False
if f:
    print("TRUTH")
else:
    print("LIE")
