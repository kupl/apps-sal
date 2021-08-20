t = int(input())
for i in range(t):
    (n, k) = list(map(int, input().split()))
    kek = k ** 2
    if n < kek:
        print('NO')
        continue
    n -= k - 1
    k = 1
    if k == 1 and n % 2 == 0:
        print('NO')
        continue
    else:
        print('YES')
