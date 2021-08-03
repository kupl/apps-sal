k1, k2, k3 = map(int, input().split())
if 1 in [k1, k2, k3]:
    print('YES')
elif sum([1 for i in [k1, k2, k3] if i == 2]) >= 2:
    print('YES')
elif sum([1 for i in [k1, k2, k3] if i == 3]) == 3:
    print('YES')
elif sum([1 for i in [k1, k2, k3] if i == 2]) == 1 and sum([1 for i in [k1, k2, k3] if i == 4]) == 2:
    print('YES')
else:
    print('NO')
