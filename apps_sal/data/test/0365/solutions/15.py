n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
su = sum(a)
if x == su and len(a) == 1:
    print('YES')
elif su == 0:
    print('YES')
elif x - su == n - 1:
    print('YES')
else:
    print('NO')
