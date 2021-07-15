n, a, b = map(int, input().split())
if a * b < n:
    print(-1)
    return

curr = 1
add = 1
res = []
for i in range(a):
    res.append([])
    for j in range(b):
        res[i].append(curr)
        curr += add
        if curr > n:
            curr = 0
            add = 0
for i in range(1, a, 2):
    res[i] = res[i][::-1]
for elem in res:
    print(' '.join(map(str, elem)))
