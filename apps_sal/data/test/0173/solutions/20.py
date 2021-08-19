(n, m) = map(int, input().split())
(h, v) = (input(), input())
if h[0] == '<' and v[0] == '^':
    print('NO')
elif h[0] == '>' and v[0] == 'v':
    print('NO')
elif h[0] == h[-1] or v[0] == v[-1]:
    print('NO')
else:
    print('YES')
