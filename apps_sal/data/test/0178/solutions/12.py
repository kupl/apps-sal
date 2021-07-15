n, s = int(input()), input()
s = s[:n-10]
a = s.count('8')
b = len(s) - a
print('YES' if a >= b else 'NO')
