def cal():
    (d, g) = list(map(int, input().split()))
    a = [list(map(int, input().split())) for i in range(d)]
    ans = float('inf')
    for i in range(2 ** d):
        b = ['-'] * d
        for j in range(d):
            if i >> j & 1:
                b[j] = '+'
        (count0, count1) = (0, 0)
        for j in range(d):
            if b[j] == '+':
                count0 += 100 * (j + 1) * a[j][0] + a[j][1]
                count1 += a[j][0]
        if count0 < g:
            for j in range(d - 1, -1, -1):
                if b[j] == '-':
                    for k in range(a[j][0]):
                        if count0 >= g:
                            break
                        count0 += 100 * (j + 1)
                        count1 += 1
        ans = min(ans, count1)
    print(ans)


cal()
