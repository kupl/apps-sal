(na, nb) = [int(i) for i in input().split()]
(k, m) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
if a[k - 1] < b[-m]:
    print('YES')
else:
    print('NO')
