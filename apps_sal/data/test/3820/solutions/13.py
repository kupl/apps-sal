(n, m) = list(map(int, input().split()))
s = input()
t = input()
if '*' not in s:
    print('YES' if s == t else 'NO')
else:
    i = s.index('*')
    print('YES' if i <= m and s[:i] == t[:i] and (n - 1 - i <= m - i) and (s[i + 1:] == t[m - (n - i - 1):]) else 'NO')
