import collections
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr = [0] + [collections.deque(arr[i]) for i in range(n)]
ans = 0
cand = set(range(1, n + 1))
while 1:
    check = set()
    for i in cand:
        if not arr[i]:
            continue
        pair = arr[i][0]
        if arr[pair][0] == i:
            check.add(i)
            check.add(pair)
    if not check:
        break
    cand = set()
    for i in check:
        cand.add(i)
        arr[i].popleft()
        if arr[i]:
            cand.add(arr[i][0])
    ans += 1
for i in range(1, n + 1):
    if arr[i]:
        print(-1)
        break
else:
    print(ans)
