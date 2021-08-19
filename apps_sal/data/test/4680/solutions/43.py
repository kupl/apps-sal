(a, b, c) = map(int, input().split())
abclist = [a, b, c]
if abclist.count(5) == 2:
    print('YES')
else:
    print('NO')
