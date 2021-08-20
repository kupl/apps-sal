def solve():
    (N, M) = list(map(int, input().split()))
    if N == 1 or M == 1:
        print('YES')
    elif N == 2 and M == 2:
        print('YES')
    else:
        print('NO')


for _ in range(int(input())):
    solve()
