def gcd(a, b):
    while (a != 0 and b != 0):
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b) // 2
n, k = [int(i) for i in input().split()]
if n <= k:
    print('-1')
else:
    a = [i + 1 for i in range(n)]
    for i in range(n - k - 1, 0, -1):
        a[i] = a[i - 1]
    a[0] = n - k
    print(*a)
