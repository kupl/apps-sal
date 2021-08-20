for n in range(int(input())):
    (a, b) = map(int, input().split())
    (c, d) = map(int, input().split())
    m1 = max(a, b)
    n1 = min(a, b)
    m2 = max(c, d)
    n2 = min(c, d)
    if m1 == m2 and n1 + n2 == m1:
        print('Yes')
    else:
        print('No')
