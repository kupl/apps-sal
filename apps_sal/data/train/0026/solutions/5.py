t = int(input())
for _ in range(t):
    (n, m) = list(map(int, input().split()))
    print('YES' if n == 1 or m == 1 or (n == 2 and m == 2) else 'NO')
