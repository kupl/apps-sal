for _ in range(int(input())):
    (a, b, c) = map(int, input().split())
    ret = float('inf')
    for da in (-1, 0, 1):
        for db in (-1, 0, 1):
            for dc in (-1, 0, 1):
                (na, nb, nc) = (a + da, b + db, c + dc)
                ret = min(ret, abs(na - nb) + abs(na - nc) + abs(nb - nc))
    print(ret)
