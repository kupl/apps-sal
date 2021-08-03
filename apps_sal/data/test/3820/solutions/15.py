input()
s = input()
t = input()

s = ' ' + s + ' '
t = ' ' + t + ' '

if '*' in s:
    idx = s.find('*')
    prefix, suffix = s[:idx], s[idx + 1:]
    print('YES' if len(s) - 1 <= len(t) and prefix == t[:len(prefix)] and suffix == t[-len(suffix):] else 'NO')
else:
    print('YES' if s == t else 'NO')
