inp = input().strip().split()
(n, m, k) = (int(inp[0]), int(inp[1]), int(inp[2]))
c1 = [-1 for i in range(m + 1)]
c2 = [-1 for i in range(m + 1)]
l = [-1 for i in range(m + 1)]
store = [False for i in range(n + 1)]
for i in range(m):
    inp = input().strip().split()
    (c1[i], c2[i], l[i]) = (int(inp[0]), int(inp[1]), int(inp[2]))
if k <= 0:
    print('-1')
else:
    inp = input().strip().split()
    ans = 1000000000 + 10
    for i in inp:
        store[int(i)] = True
    for i in range(m):
        (x, y, d) = (c1[i], c2[i], l[i])
        if store[x] and (not store[y]):
            ans = min(ans, d)
        if store[y] and (not store[x]):
            ans = min(ans, d)
    if ans == 1000000000 + 10:
        print('-1')
    else:
        print(ans)
