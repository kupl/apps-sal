def check_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


t = int(input())
for tnum in range(t):
    (a, b) = map(int, input().split())
    if a != b + 1:
        print('NO')
    else:
        print('YES' if check_prime(a + b) else 'NO')
