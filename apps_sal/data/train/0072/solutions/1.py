for i in range(int(input())):
    (n, k) = (int(j) for j in input().split())
    a = [int(j) for j in input().split()]
    mm = set(a)
    if len(mm) > k:
        print('-1', end=' ')
    else:
        if len(mm) < k:
            for j in range(1, 101):
                if j not in mm:
                    mm.add(j)
                if len(mm) == k:
                    break
        print(n * len(mm))
        for j in range(n):
            print(' '.join((str(x) for x in mm)), end=' ')
    print()
