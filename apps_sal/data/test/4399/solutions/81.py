from sys import stdin, stdout
for _ in range(1):
    s = len(set(input()))
    print('Yes' if s > 1 else 'No')
