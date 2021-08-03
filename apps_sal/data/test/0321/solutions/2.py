def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

    return True


for i in ' ' * int(input()):
    a, b = map(int, input().split())
    if a - b > 1:
        print('NO')
    else:
        print(['NO', 'YES'][isPrime(a + b)])
