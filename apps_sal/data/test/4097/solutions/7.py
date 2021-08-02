n = int(input())
m = list(map(int, input().split()))
if n == 1:
    print(0)
else:
    sost = [-1, 0, 1]
    mi = int(1e10)
    for elem in sost:
        for elem2 in sost:
            new_m = m.copy()
            cur_mi = (elem != 0) + (elem2 != 0)
            start = elem + m[0]
            end = elem2 + m[-1]
            new_m[0] = start
            new_m[-1] = end
            f = True
            if abs(start - end) % (n - 1) == 0:
                step = (start - end) // (n - 1)
                for i in range(1, n - 1):
                    if new_m[i - 1] - new_m[i] != step:
                        if abs(new_m[i - 1] - new_m[i] - step) == 1:
                            cur_mi += 1
                            new_m[i] += (new_m[i - 1] - new_m[i] - step)
                        else:
                            f = False
                            break
                if f:
                    mi = min(mi, cur_mi)
    if mi == int(1e10):
        print(-1)
    else:
        print(mi)
