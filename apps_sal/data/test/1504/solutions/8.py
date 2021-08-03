t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    l1, r1 = list(map(int, input().split()))
    l2, r2 = list(map(int, input().split()))
    mr = max(r1, r2) - min(l1, l2)
    step = 2 * mr - (r1 - l1) - (r2 - l2)
    over = max(0, min(r1, r2) - max(l1, l2))
    dis = (max(l1, l2) - min(r1, r2)) if over == 0 else 0
    k = k - over * n
    if k <= 0:
        print(0)
        continue
    mr -= over
    res = 0
    if k <= mr:
        res = dis + k
    elif mr * n >= k:
        cnt = k // mr
        r = k % mr
        res += cnt * step
        if r > dis:
            res += dis + r
        else:
            res += 2 * r
    else:
        res += n * step + (k - mr * n) * 2
    print(res)
