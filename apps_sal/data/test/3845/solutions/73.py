ab = list(map(int, input().split()))

g = [['
for k in range(2):
    cnt = 0
    flag = False
    c = '.' if k == 0 else '
    for i in range(51 * k, 50 * (k + 1), 2):
        for j in range(0, 100, 2):
            if cnt == ab[k] - 1:
                flag = True
                break
            g[i][j] = c
            cnt += 1
        if flag:
            break
print((100, 100))
for i in g:
    print((''.join(i)))
