n = int(input())
s = ''.join(('1' if c == 'R' else '0' for c in input()[::-1]))
d = int(s, 2)
print((1 << n) - 1 - d)
