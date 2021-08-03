n = int(input())

a = [int(input()) for _ in range(n)]

s = list(set(a))
if len(s) == 2 and a.count(s[0]) == a.count(s[1]):
    print('YES')
    print(*s)
else:
    print('NO')
