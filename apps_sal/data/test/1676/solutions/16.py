n, b = [int(i) for i in input().split()]
q = [0] * n
bg = 0
en = 0
time = 0
res = [-1] * n
for it in range(n):
    ev = [int(i) for i in input().split()]
    ev.append(it)
    while bg < en and max(time, q[bg][0]) <= ev[0]:
        time = max(time, q[bg][0])
        res[q[bg][2]] = time + q[bg][1]
        time += q[bg][1]
        bg += 1
    if en - bg < b:
        q[en] = ev
        en += 1
        
while bg < en:
    time = max(time, q[bg][0])
    res[q[bg][2]] = time + q[bg][1]
    time += q[bg][1]
    bg += 1

for i in range(n):
    print(res[i], end=' ')

