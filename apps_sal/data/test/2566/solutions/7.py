t = int(input())
while t:
    k = int(input())
    a = [int(i) for i in input().split()]
    da = [999] * 8
    cnt = sum(a)
    for i in range(0, 7):
        if not a[i]:
            continue
        tmp_cnt = 0
        for j in range(0, 7):
            x = (i + j) % 7
            if not a[x]:
                continue
            tmp_cnt += 1
            da[tmp_cnt] = min(da[tmp_cnt], j + 1)
    if k % cnt:
        print(k // cnt * 7 + da[k % cnt])
    else:
        print(k // cnt * 7 - 7 + da[cnt])
    t -= 1
