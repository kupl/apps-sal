n = int(input())
print(n // 2)
k = ['2' for i in range(n // 2)]
if (n % 2): k[-1] = '3'
print(' '.join(k))
