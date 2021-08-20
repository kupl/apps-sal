p = input().split()
a = int(f'{p[0]}{p[1]}')
print('Yes' if a == int(a ** 0.5) ** 2 else 'No')
