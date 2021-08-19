t = int(input())
for _ in range(t):
    (a, b, n, s) = list(map(int, input().split()))
    coins = min(s // n, a)
    s = s - coins * n
    if s <= b:
        print('YES')
    else:
        print('NO')
