(a, b) = list(map(int, input().split()))
queue = [a]
qstart = 0
prev = dict()
prev[a] = -1
while qstart + 1 <= len(queue):
    our = queue[qstart]
    qstart += 1
    if our * 2 <= 10 ** 9 and our * 2 not in prev:
        queue.append(our * 2)
        prev[our * 2] = our
    t = our * 10 + 1
    if t <= 10 ** 9 and t not in prev:
        queue.append(t)
        prev[t] = our
if b in prev:
    print('YES')
    res = []
    curr = b
    while curr != -1:
        res.append(curr)
        curr = prev[curr]
    print(len(res))
    print(' '.join(map(str, res[::-1])))
else:
    print('NO')
