for _ in range(int(input())):
    (n, m, k) = list(map(int, input().split()))
    hi = None
    for hi1 in map(int, input().split()):
        if hi is not None:
            m += hi
            if m + k < hi1:
                print('NO')
                break
            if hi1 > k:
                m -= hi1 - k
        hi = hi1
    else:
        print('YES')
