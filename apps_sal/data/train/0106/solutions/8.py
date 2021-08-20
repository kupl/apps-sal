t = int(input())
for tc in range(t):
    n = int(input())
    l = []
    for i in range(n):
        (a, b) = map(int, input().split())
        l.append([i, a, b])
    l = sorted(l, key=lambda x: x[1])
    last = l[0][1]
    i = 0
    while i < n:
        if l[i][1] > last:
            break
        last = max(last, l[i][2])
        i += 1
    if i == n:
        print(-1)
    else:
        ind = [2] * n
        for j in range(i):
            ind[l[j][0]] = 1
        for i in ind:
            print(i, end=' ')
        print('')
