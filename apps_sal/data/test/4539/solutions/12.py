n = int(input())
a = sum(map(int, list(str(n))))
print('Yes' if n % a == 0 else 'No')
