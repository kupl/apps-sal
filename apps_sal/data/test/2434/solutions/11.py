q = int(input())
for irweewr in range(q):
    (n, m) = map(int, input().split())
    if n % m == 0:
        print('YES')
    else:
        print('NO')
