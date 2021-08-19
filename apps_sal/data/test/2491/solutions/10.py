(n, m) = map(int, input().split())
edge = [list(map(int, input().split())) for i in range(m)]
node = [-float('inf') for i in range(n + 1)]
node[1] = 0
inf = False
for i in range(2 * n + 1):
    loop = False
    for (s, e, c) in edge:
        if node[e] < node[s] + c:
            node[e] = node[s] + c
            if e == n:
                loop = True
    if i >= n and loop:
        inf = True
        break
if inf:
    print('inf')
else:
    print(node[-1])
