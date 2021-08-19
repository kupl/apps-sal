t = int(input())
for case in range(t):
    (n, k) = list(map(int, input().split()))
    sum_k = k * k
    if n % 2 == sum_k % 2 and n >= sum_k:
        print('YES')
    else:
        print('NO')
