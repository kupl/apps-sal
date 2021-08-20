n = int(input())
if n % 2 == 0:
    print(-1)
else:
    print(' '.join(map(str, list(range(0, n)))))
    il = [0]
    for i in range(1, n):
        if i <= n // 2:
            il.append(n - 2 * i)
        else:
            il.append(n - 1 - 2 * (i - n // 2 - 1))
    print(' '.join(map(str, il)))
    print(' '.join(map(str, [(i + il[i]) % n for i in range(0, n)])))
