[n, m] = list(map(int, input().split()))
p = list(map(int, input().split()))
for i in range(m):
    [l, r, x] = list(map(int, input().split()))
    a = p[x - 1]
    cnt = 0
    for j in range(l, r + 1):
        if p[j - 1] <= a:
            cnt += 1
    if cnt == x - l + 1:
        print('Yes')
    else:
        print('No')
