n, m = list(map(int, input().split()))
d = {}
for i in range(m):
    t, o = input().split()
    if o in d:
        d[o].append(t)
    else:
        d[o] = [t]

q = [('a', 0)]
cnt = 0
while q and q[0][1] < n:
    st = q[0]
    q.pop(0)
    if st[1] == n - 1:
        cnt += 1
    if st[0][0] in d:
        for j in d[st[0][0]]:
            q.append((j + st[0][1:], st[1] + 1))

print(cnt)
