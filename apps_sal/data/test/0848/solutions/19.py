n, k = map(int, input().split())
a = n * (n - 1) // 2
if(n * k > a):
    print(-1)
else:
    l = [str(n * k)]
    for i in range(1, n + 1):
        for j in range(k):
            l.append(str(i) + ' ' + str((i + j) % n + 1))
    print('\n'.join(l))
