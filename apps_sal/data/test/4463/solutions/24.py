s = ''.join(sorted(list(input())))
t = ''.join(sorted(list(input()))[::-1])
print('Yes' if s < t else 'No')
