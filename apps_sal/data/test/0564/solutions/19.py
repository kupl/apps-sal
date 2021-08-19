(n, s) = tuple(map(int, str.split(input())))
if sum(sorted(map(int, str.split(input())))[:-1]) <= s:
    print('YES')
else:
    print('NO')
