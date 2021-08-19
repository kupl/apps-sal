for t in range(1):
    (n, q) = map(int, input().split())
    time = [0] * n
    for i in range(q):
        (t, k, d) = map(int, input().split())
        count = 0
        pos = 0
        for j in range(n):
            if time[j] <= t:
                pos += j + 1
                count += 1
            if count == k:
                break
        if count < k:
            print(-1)
            continue
        changed = 0
        for j in range(n):
            if time[j] <= t:
                time[j] = t + d
                changed += 1
            if changed == count:
                break
        print(pos)
