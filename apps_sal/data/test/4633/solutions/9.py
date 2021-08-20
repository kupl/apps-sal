for _ in range(int(input())):
    (n, s) = map(int, input().split())
    savn = n
    cd = 1
    while cd <= n:
        if sum(map(int, str(n))) <= s:
            break
        cc = n // cd % 10
        if cc == 0:
            cd *= 10
            continue
        n += (10 - cc) * cd
        cd *= 10
    print(n - savn)
