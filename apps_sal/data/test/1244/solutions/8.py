3
n = int(input())
a = list(map(int, input().split()))
m = max((len([1 for w in a if w == v]) for v in a))
if 2 * m <= n + 1:
    print('YES')
else:
    print('NO')
