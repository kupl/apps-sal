input()
s = input()
t = input()
if s.count('*'):
    for i in range(len(s)):
        if s[i] == '*':
            print('YES' if s[0:i] == t[0:i] and s[i + 1:] == t[len(t) - len(s[i + 1:]):] and i <= len(t) - len(s[i + 1:]) else 'NO')
            return
else:
    print('YES' if s == t else 'NO')
