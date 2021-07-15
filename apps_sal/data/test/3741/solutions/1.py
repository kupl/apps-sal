from collections import Counter, deque

n = int(input())
arr = list([x for x in map(int, input().strip().split()) if x != 0])

'''
for i, a in enumerate(arr):
    for j, b in enumerate(arr):
        if a & b != 0 and i != j:
            print(i,j,a,b)
return
'''

c = Counter()

for each in arr:
    for b in range(0, 64):
        if (1 << b) & each != 0:
            c[b] += 1
            if c[b] >= 3:
                print(3)
                return

ans = 1234567

for idx, st in enumerate(arr):
    dists = {}
    q = deque()
    q.append((idx, -1))
    dists[idx] = 0

    while q:
        node, par = q[0]
        dist = dists[node]
        q.popleft()
        for idx2, v in enumerate(arr):
            if idx2 == par:
                continue
            if idx2 == node or (v & arr[node]) == 0:
                continue
            if idx2 in dists:
                candidate = dists[idx2] + dist + 1
                if candidate != 2:
                    ans = min(ans, candidate)
                continue
            dists[idx2] = dist + 1
            q.append((idx2, node))


if ans == 1234567:
    print(-1)
else:
    print(ans)

