a = input().split(' ')
n = int(a[0])
k = int(a[1])
a = input().split(' ')
a = [int(i) for i in a]
if k > n - 1:
    print(max(a))
    return
wf = 0
c = 0
cw = a[0]
for i in range(1, n - 1):
    cw = max(cw, a[i])
    if a[i] == cw:
        c = 1
        continue
    c = c + 1
    if c >= k:
        wf = cw
        print(wf)
        break
else:
    print(max(a))
