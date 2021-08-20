def __starting_point():
    n = int(input())
    arr = [None] * (n + 3)
    cnt = 1
    for i in range(2, n + 1):
        if not arr[i]:
            for j in range(i, n + 1, i):
                if not arr[j]:
                    arr[j] = cnt
            cnt += 1
    print(' '.join(map(str, arr[2:n + 1])))


__starting_point()
