a = int(input())
b = input()
c = b[:a // 2]
d = b[a // 2:a]
print('Yes' if c == d else 'No')
