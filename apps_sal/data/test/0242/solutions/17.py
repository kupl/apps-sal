def zeroes(x):
    n = 0
    while x:
        d = x // 5
        n += d
        x = d
    return n


m = int(input())
i = 0
j = 500000
while j - i > 1:
    k = (i + j) // 2
    n = zeroes(k)
    if n < m:
        i = k
    elif n > m:
        j = k
    else:
        k = k // 5 * 5
        print(5)
        print(' '.join([str(k + i) for i in range(5)]))
        break
else:
    print(0)
