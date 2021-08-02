n, k = tuple(map(int, input().split()))

if (n - 1) // 2 < k:
    print(-1)
else:
    answer = []
    m = n * k
    print(m)
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            a = i
            b = (i + j) % n
            if not b:
                b = n
            answer.append(str(a) + ' ' + str(b))
    print('\n'.join(answer))
