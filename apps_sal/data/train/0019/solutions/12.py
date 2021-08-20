for i in range(int(input())):
    a = list(map(int, input().split()))
    (n, k, d) = (a[0], a[1], a[2])
    a = list(map(int, input().split()))
    di = dict()
    m = 0
    m2 = 1000000
    n2 = 0
    for j in range(len(a)):
        if n2 < d:
            if a[j] not in di:
                di[a[j]] = 1
                m += 1
            else:
                if di[a[j]] == 0:
                    m += 1
                di[a[j]] += 1
            n2 += 1
        else:
            if di[a[j - d]] == 1:
                di[a[j - d]] = 0
                m -= 1
            else:
                di[a[j - d]] -= 1
            if a[j] not in di:
                di[a[j]] = 1
                m += 1
            else:
                if di[a[j]] == 0:
                    m += 1
                di[a[j]] += 1
        if n2 == d and m < m2:
            m2 = m
    print(m2)
