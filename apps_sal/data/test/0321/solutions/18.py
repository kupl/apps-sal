def isprime(n):
    i = 2
    m = n
    while i * i <= n:
        while n % i == 0:
            n /= i
        i += 1
    return m == n


t = int(input())
for i in range(t):
    (a, b) = map(int, input().split())
    if isprime(a + b) and a - b == 1:
        print('YES')
    else:
        print('NO')
