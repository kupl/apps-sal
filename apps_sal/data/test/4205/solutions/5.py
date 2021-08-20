N = int(input())
p = list(map(int, input().split()))
if p == sorted(p):
    print('YES')
else:
    ret = 'NO'
    is_sorted = False
    for i in range(N - 1):
        for j in range(i + 1, N):
            if p[i] < p[j]:
                continue
            else:
                k = p.copy()
                (k[i], k[j]) = (k[j], k[i])
            if k == sorted(p):
                ret = 'YES'
                is_sorted = True
                break
        if is_sorted:
            break
    print(ret)
