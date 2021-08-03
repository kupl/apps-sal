t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    if n == 1 or m == 1 or (m == 2 and n == 2):
        print('YES')
    else:
        print('NO')
