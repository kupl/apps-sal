s = input()
n = len(s)
print(s[(n + 1) // 2:].count('g') - s[:(n + 1) // 2].count('p'))
