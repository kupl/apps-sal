n = int(input())
a = list(map(int, input().split()))
a = len(list(set(a)))
if n == a:
    print('YES')
else:
    print('NO')
