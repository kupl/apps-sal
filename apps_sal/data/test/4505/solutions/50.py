s = list(input())
s.sort()
print('Yes' if s[0] + s[1] + s[2] == 'abc' else 'No')
