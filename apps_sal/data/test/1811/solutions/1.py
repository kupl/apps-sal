3

n, k = tuple(map(int, input().split()))
t = [_ for _ in input().split('.') if len(_) >= k]
if t:
    print('NO')
else:
    print('YES')


