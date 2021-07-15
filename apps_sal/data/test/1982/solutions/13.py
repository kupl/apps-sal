t = int(input())
for test_i in range(t):
    n, k = map(int, input().split())
    if n % 2 == k % 2 and n >= k * k:
        print('YES')
    else:
        print('NO')
