n = int(input())
tp = []
tmp = 10**15
for _ in range(5):
    a = int(input())
    if tmp > a:
        tmp = a
    tp.append(a)

if tmp >= n:
    print(5)
    return

cnt = n//tmp
mod = n%tmp

if mod > 0:
    print(5+cnt)
else:
    print(5+cnt-1)
