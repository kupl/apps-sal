(n, k) = list(map(int, input().split()))
print((6 * n - 1) * k)
print('\n'.join(('%i %i %i %i' % tuple((k * (6 * i + j) for j in (1, 2, 3, 5))) for i in range(n))))
