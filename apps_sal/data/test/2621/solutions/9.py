t = int(input())
for _ in range(t):
    (n, m, k) = list(map(int, input().split()))
    h = list(map(int, input().split()))
    block = m
    flag = 1
    for i in range(n - 1):
        if h[i + 1] - k <= h[i]:
            block += min(h[i], h[i] - (h[i + 1] - k))
        elif h[i + 1] - k - h[i] > block:
            flag = 0
            break
        else:
            block -= h[i + 1] - k - h[i]
    if flag == 1:
        print('YES')
    else:
        print('NO')
