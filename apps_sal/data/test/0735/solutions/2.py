n = int(input())
a = list(map(int, input().split()))
phase = 0
l = -1
r = -1
for i in range(1, len(a)):
    g = a[i] > a[i-1]
    if phase == 0 and not g:
        l = i
        phase = 1
    if phase == 1 and g:
        r = i
        phase = 2
    if phase == 2 and not g:
        print('no')
        return
if phase == 0:
    print('yes')
    print('1 1')
    return
elif phase == 1:
    r = len(a)
cur = -1
f = True
for i in range(0, l-1):
    if a[i] < cur:
        f = False
        break
    cur = a[i]
for i in range(r-1, l-2, -1):
    if a[i] < cur:
        f = False
        break
    cur = a[i]
for i in range(r, len(a)):
    if a[i] < cur:
        f = False
        break
    cur = a[i]
if f:
    print('yes')
    print(l, r)
else:
    print('no')

