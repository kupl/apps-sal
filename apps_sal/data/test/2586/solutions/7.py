t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    print('WB' + (m - 2) * 'B')
    for _ in range(n - 1):
        print(m * 'B')
