n = int(input())
l = [0, 3, 4, 5, 6, 8]
print('NYOE S'[n == 12 or (n // 10 in l and n % 10 in [2] + l)::2])
