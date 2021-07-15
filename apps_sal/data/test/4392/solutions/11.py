for _ in range(int(input())):
    n, m = map(int, input().split())
    l = [*map(int, input().split())]
    p = sorted([*map(int, input().split())])
    for _ in range(n):
        for i in p:
            l[i - 1], l[i] = sorted(l[i - 1 : i + 1])
    print(['NO', 'YES'][l == sorted(l)])
