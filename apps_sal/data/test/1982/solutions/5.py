q = int(input())
for rweur in range(q):
    (n, k) = map(int, input().split())
    if (n - k) % 2 == 1:
        print('NO')
    elif n >= k ** 2:
        print('YES')
    else:
        print('NO')
