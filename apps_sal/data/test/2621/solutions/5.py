t = int(input())
for _ in range(t):
    (n, m, k) = map(int, input().split())
    h = list(map(int, input().split()))
    possible = True
    cur_h = h[0]
    for next_h in h[1:]:
        if cur_h + k < next_h:
            needed = next_h - cur_h - k
            if needed > m:
                possible = False
                break
            m -= needed
        else:
            m += min(cur_h, cur_h - (next_h - k))
        cur_h = next_h
    if possible:
        print('YES')
    else:
        print('NO')
