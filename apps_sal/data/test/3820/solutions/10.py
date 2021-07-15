n, m = map(int, input().split())
s = input()
t = input()
if len(s) - 1 > m:
    print('NO')
elif s == '*':
    print('YES')
elif '*' not in s:
    if s == t:
        print('YES')
    else:
        print('NO')
else:
    for i in range(len(s)):
        if s[i] == '*':
            pos = i
            break
    if s[0 : pos] == t[0 : pos] and s[pos + 1:] == t[m - (n - pos) + 1:]:
        print('YES')
    else:
        print('NO')
