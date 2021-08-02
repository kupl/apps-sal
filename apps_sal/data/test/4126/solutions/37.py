s = input()

a = s[:len(s) // 2]
b = s[len(s) // 2 + 1:]
print('Yes' if s == s[::-1] and a == a[::-1] and b == b[::-1] else 'No')
