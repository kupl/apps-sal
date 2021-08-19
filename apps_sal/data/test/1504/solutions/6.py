t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    (l1, r1) = list(map(int, input().split()))
    (l2, r2) = list(map(int, input().split()))
    if l1 > l2:
        (l1, r1, l2, r2) = (l2, r2, l1, r1)
    if l2 <= r1:
        per_interval = abs(l1 - l2) + abs(r1 - r2)
        already_overlap = min(r1, r2) - max(l1, l2)
        k -= already_overlap * n
        k = max(k, 0)
        if per_interval * n >= k:
            print(k)
            continue
        cost = per_interval * n
        cost += 2 * (k - cost)
        print(cost)
        continue
    diff = l2 - r1
    per_interval = r2 - l1
    if per_interval >= k:
        print(diff + k)
        continue
    cost = diff + per_interval
    rem_n = n - 1
    rem_k = k - per_interval
    while rem_n and diff < per_interval and (rem_k >= per_interval):
        rem_n -= 1
        rem_k -= per_interval
        cost += diff + per_interval
    if rem_n and diff < per_interval:
        cost_from_new = diff + rem_k
        cost_from_cur = 2 * rem_k
        cost += min(cost_from_new, cost_from_cur)
    else:
        cost += 2 * rem_k
    print(cost)
