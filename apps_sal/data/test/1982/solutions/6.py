T = int(input())
for case in range(T):
    (n, k) = [int(x) for x in input().split(' ')]
    if (n - k) % 2 == 0 and n >= k * k:
        print('YES')
    else:
        print('NO')
