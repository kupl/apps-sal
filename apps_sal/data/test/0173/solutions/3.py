(n, m) = map(int, input().split())
s = input()
t = input()
if s[0] == '>' and t[0] == 'v' or (s[0] == '<' and t[0] == '^') or (s[0] == '>' and t[m - 1] == '^') or (s[0] == '<' and t[m - 1] == 'v') or (s[n - 1] == '>' and t[0] == '^') or (s[n - 1] == '<' and t[0] == 'v'):
    print('NO')
else:
    print('YES')
