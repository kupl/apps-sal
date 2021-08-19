t = int(input())


def solve(n, m):
    for i in range(n):
        if i == 0:
            print('W' + 'B' * (m - 1))
        else:
            print('B' * m)


for _ in range(t):
    (n, m) = list(map(int, input().split()))
    solve(n, m)
