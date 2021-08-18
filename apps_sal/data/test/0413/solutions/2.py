def two_degree(n, m):
    deg = 0
    res = n
    while res < m:
        res *= 2
        deg += 1
    print(res)
    return deg, res - m


my_str = input()
n, m = int(my_str.split()[0]), int(my_str.split()[1])
if m < n:
    print(n - m)
else:
    res = n
    oper = 0
    while res != m:
        if m % 2 == 1 and m > res:
            m += 1
            oper += 1
        elif m > res:
            m = int(m / 2)
            oper += 1
        elif m < res:
            oper += (res - m)
            m = res
    print(oper)
