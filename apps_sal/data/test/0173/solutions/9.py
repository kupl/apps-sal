(n, m) = list(map(int, input().split()))
a = input()
b = input()
if a[0] == '>' and a[n - 1] == '<' and (b[0] == '^') and (b[m - 1] == 'v'):
    print('YES')
elif a[n - 1] == '>' and a[0] == '<' and (b[m - 1] == '^') and (b[0] == 'v'):
    print('YES')
else:
    print('NO')
