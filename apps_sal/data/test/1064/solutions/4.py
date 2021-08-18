import sys

n, m, k = list(map(int, input().split()))
s = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))

if m > 0 and s[0] == 0:
    print('-1')
else:

    block = [-1] * n
    for i in range(m):
        if block[s[i] - 1] == -1:
            block[s[i]] = s[i] - 1
        else:
            block[s[i]] = block[s[i] - 1]

    MAX_COST = 1e13
    max_inr = 0
    if m > 0:
        inr = 1
        prev = s[0]
        for i in range(1, m):
            if s[i] == prev + 1:
                inr += 1
            else:
                if inr > max_inr:
                    max_inr = inr
                inr = 1
            prev = s[i]
        if inr > max_inr:
            max_inr = inr
    best_cost = []
    for i in range(k):
        if i < max_inr:
            best_cost.append(MAX_COST)
        else:
            best_cost.append(a[i] * (-(-n // (i + 1))))
    min_cost = MAX_COST
    for i in range(k):
        test = i
        if best_cost[test] >= min_cost:
            continue
        t_size = test + 1
        pos = 0
        count = 1
        while pos < n:
            new_pos = pos + t_size
            if new_pos >= n:
                break
            if block[new_pos] != -1:
                if block[new_pos] <= pos:
                    raise Exception('smth went wrong')
                new_pos = block[new_pos]
            pos = new_pos
            count += 1
        min_cost = min(min_cost, a[test] * count)
    if min_cost < MAX_COST:
        print(min_cost)
    else:
        print('-1')
