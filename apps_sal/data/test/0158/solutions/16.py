n = int(input())
a = [int(x) for x in input().split()]
assert len(a) == n + n
a.sort()
if a[n - 1] < a[n]:
    print('YES')
else:
    print('NO')
