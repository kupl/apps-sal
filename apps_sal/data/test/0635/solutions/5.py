(n, s) = list(map(int, input().split()))
s -= 1
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if a[0] == 0:
    print('NO')
elif a[s] == 1:
    print('YES')
elif b[s] == 0:
    print('NO')
elif any([x[0] == x[1] == 1 for x in zip(a[s:], b[s:])]):
    print('YES')
else:
    print('NO')
