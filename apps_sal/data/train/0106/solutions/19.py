T = int(input())
for _ in range(T):
    n = int(input())
    events = []
    results = [0 for i in range(n)]
    fail = False
    for i in range(n):
        (l, r) = map(int, input().split())
        events.append((l, 0, i))
        events.append((r, 1, i))
    events.sort()
    cnt = 0
    cur_seg = 1
    for (_, t, i) in events:
        if t == 0:
            cnt += 1
            results[i] = cur_seg
        else:
            cnt -= 1
        if cnt == 0:
            cur_seg = 1 + cur_seg % 2
    if len(set(results)) == 2:
        print(*results)
    else:
        print(-1)
