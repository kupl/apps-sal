t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    print('W' + (m - 1) * 'B')
    for j in range(n - 1):
        print('B' * m)
