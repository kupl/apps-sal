t = int(input())
for _ in range(t):
    (a, b) = list(map(int, input().split()))
    print('YES' if a > b + 1 else 'NO')
