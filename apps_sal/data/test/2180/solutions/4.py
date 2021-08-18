n = int(input())

if n % 2 == 0:
    print(n * n // 2)
    print('\n'.join([('C.' if i % 2 == 0 else '.C') * (n // 2) for i in range(n)]))
else:
    p = n // 2
    q = (n + 1) // 2
    print(p * p + q * q)
    print('\n'.join([('C.' * p + 'C') if i % 2 == 0 else ('.C' * p + '.') for i in range(n)]))
