(n, m) = list(map(int, input().split()))
l = [0] * (m + 1)
l[0] = 1
for i in range(n):
    (a, b) = list(map(int, input().split()))
    for i in range(a + 1, b + 1):
        l[i] = 1
if 0 in l:
    print('NO')
else:
    print('YES')
