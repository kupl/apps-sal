n = int(input())
a = list((map(int, input().split())))
b = list((map(int, input().split())))
k, l = a[0], b[0]
a.pop(0)
b.pop(0)
cnt = 0
while len(a) > 0 and len(b) > 0 and cnt < 1000:
    if a[0] > b[0]:
        a.append(b[0])
        a.append(a[0])

    if b[0] > a[0]:
        b.append(a[0])
        b.append(b[0])

    cnt += 1
    a.pop(0)
    b.pop(0)
if len(a) == 0:
    print(cnt, 2)
    quit()
if len(b) == 0:
    print(cnt, 1)
    quit()
if len(a) > 0 and len(b) > 0:
    print(-1)
else:
    print(cnt)
