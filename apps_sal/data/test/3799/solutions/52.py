s = input()
x = (len(s) + (s[0] == s[-1])) % 2
print('First' * x + 'Second' * (1 - x))
