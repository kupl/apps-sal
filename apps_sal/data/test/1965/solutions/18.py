def read_line():
    return list(map(int, input().split()))


T = int(input())
for _ in range(T):
    (n, x) = list(map(int, input().split()))
    l = read_line()
    t = 0
    all_eq = True
    has_eq = False
    for a in l:
        t += a - x
        if a != x:
            all_eq = False
        else:
            has_eq = True
    if all_eq:
        print(0)
    elif t == 0 or has_eq:
        print(1)
    else:
        print(2)
