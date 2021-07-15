n = int(input())
a = [int(input()) for i in range(n)]
b = list(set(a))
if len(b) == 2 and a.count(b[0]) == a.count(b[1]) == n // 2:
    print('YES')
    print(*b)
else:
    print('NO')
