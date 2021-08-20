s = input()
if s.find('AB') != -1 and s[s.find('AB') + 2:].find('BA') != -1 or (s.find('BA') != -1 and s[s.find('BA') + 2:].find('AB') != -1):
    print('YES')
else:
    print('NO')
