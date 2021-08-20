T = int(input())
for _ in range(T):
    (N, K) = map(int, input().split())
    if N >= K * K and (N - K) % 2 == 0:
        print('YES')
    else:
        print('NO')
