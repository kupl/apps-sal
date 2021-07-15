n = input()
s = sum(map(int, list(n)))
print('Yes' if int(n) % s == 0 else 'No')
