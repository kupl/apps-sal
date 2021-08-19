n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append(a[i])
b.sort()
f = -1
l = 0
for i in range(n):
    if a[i] != b[i]:
        if f == -1:
            f = i
        l = i
if f != -1:
    c = a[:f]
    if f != 0:
        c += a[l:f - 1:-1]
    else:
        c += a[l::-1]
    c += a[l + 1:]
else:
    f = 0
    c = a
flag = True
for i in range(n):
    if b[i] != c[i]:
        flag = False
if flag:
    print('yes')
    print(f + 1, l + 1)
else:
    print('no')
