for _ in range(int(input())):
    (n, m) = map(int, input().split())
    List = [int(x) for x in input().split()]
    if sum(List) == m:
        print('YES')
    else:
        print('NO')
