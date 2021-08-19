(n, m) = map(int, input().split())
s = input()
t = input()
index = s.find('*')
if n - m > 1:
    print('NO')
elif s[:index] == t[:index] and s[index + 1:] == t[m - len(s[index + 1:]):]:
    print('YES')
else:
    print('NO')
