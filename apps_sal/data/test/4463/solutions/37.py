(a, b) = [sorted(input()) for i in range(2)]
print('Yes' if a < b[::-1] else 'No')
