(n, m) = list(map(int, input().split()))
a = input()
b = input()
if a[0] == '>' and b[0] == 'v' or (a[0] == '<' and b[-1] == 'v') or (a[-1] == '>' and b[0] == '^') or (a[-1] == '<' and b[-1] == '^'):
    print('NO')
else:
    print('YES')
