N = int(input())
p = list(map(int, input().split()))
if p == sorted(p):
    print('YES')
else:
    ret = 'NO'
    for i in range(N - 1):
        for j in range(i + 1, N):
            if p[i] < p[j]:
                is_sorted = False
                continue
            else:
                k = p.copy()
                (k[i], k[j]) = (k[j], k[i])
            is_sorted = True
            for l in range(N - 1):
                if k[l + 1] < k[l]:
                    is_sorted = False
                    break
            if is_sorted:
                ret = 'YES'
                break
        if is_sorted:
            break
    print(ret)
