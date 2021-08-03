n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

karms = []
for i in arr:
    t = []
    while i > 0:
        t.append(i)
        i //= 2
    t.append(0)
    karms.append(t)

# print(*karms)

ans = 1e15
for i in range(0, arr[-1] + 1):
    count = 0
    for karm in karms:
        if i in karm:
            count += 1
        if count == k:
            break

    if count < k:
        continue
    adds = []
    for karm in karms:
        if i not in karm:
            continue
        adds.append(karm.index(i))
        if len(adds) == k:
            break
    ans = min(ans, sum(adds))

print(ans)
