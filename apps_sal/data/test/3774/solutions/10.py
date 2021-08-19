(n, m) = [int(x) for x in input().split()]


def cal(n, m):
    if n < m:
        (n, m) = (m, n)
    if m == 1:
        dt = {0: 0, 1: 1, 2: 2, 3: 3, 4: 2, 5: 1}
        return dt[n % 6]
    if n == 7:
        if m == 2:
            return 2
        return n * m % 2
    elif n >= 4:
        return n * m % 2
    else:
        dt = {(3, 2): 2, (3, 1): 3, (2, 2): 4, (2, 1): 2}
        return dt.get((n, m), n * m % 2)


print(n * m - cal(n, m))
