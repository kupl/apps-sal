s = input()
m = s.count(s[0])
print('Yes' if m == 2 and len(set(s)) == 2 else 'No')
