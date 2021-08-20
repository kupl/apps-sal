for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    (n, m) = (min(a), max(a))
    b = [m - x for x in a]
    c = [x - n for x in a]
    if k & 1:
        print(*b)
    else:
        print(*c)
