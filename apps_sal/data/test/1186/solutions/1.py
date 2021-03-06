from math import log2, floor
n = int(input())
if n % 2:
    print('NO')
else:
    print('YES')
    k = floor(log2(n)) + 1
    res = [0 for i in range(n)]
    occupied = [0 for i in range(n)]
    switch = 0
    for i in range(n, 0, -1):
        val = 2 ** k - 1 - i
        if val > n:
            k -= 1
            val = 2 ** k - 1 - i
        if occupied[val - 1]:
            while occupied[val - 1]:
                k -= 1
                val = 2 ** k - 1 - i
        val = 2 ** k - 1 - i
        occupied[val - 1] = 1
        res[i - 1] = val
    for i in res:
        print(i, end=' ')
    print()
if n in [1, 2, 3, 4, 5]:
    print('NO')
elif int(log2(n)) == log2(n):
    print('NO')
elif n == 6:
    print('YES')
    print('3 6 2 5 1 4')
else:
    print('YES')
    print('7 3 2 5 6 4 1', end=' ')
    for i in range(8, n):
        p = pow(2, floor(log2(i)) + 1)
        if i < pow(2, floor(log2(n))):
            print(p * 3 // 2 - 1 - i, end=' ')
        else:
            print(i + 1, end=' ')
    if n > 7:
        print(pow(2, floor(log2(n))))
