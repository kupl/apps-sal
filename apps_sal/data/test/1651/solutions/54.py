(s, p) = map(int, input().split())


def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    return table


l = divisor(p)
l = sorted(l)
len_l = len(l)
check = 0
if len(l) % 2 == 0:
    for i in range(0, len_l // 2):
        (a, b) = (l[i], l[len_l - i - 1])
        if a + b == s:
            check = 1
else:
    for i in range(0, len_l // 2):
        (a, b) = (l[i], l[len_l - i - 1])
        if a + b == s:
            check = 1
    if l[len_l // 2] * 2 == s:
        check = 1
if check:
    print('Yes')
else:
    print('No')
