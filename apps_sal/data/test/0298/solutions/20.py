(n, k) = (int(i) for i in input().split())
a = n // k
print('YES' if a % 2 == 1 else 'NO')
