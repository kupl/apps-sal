def solve():
    A = list(map(int, input().split()))
    p1 = A[0] - 1
    p2 = A[0]
    fat = 1

    A[1] = A[1] - 1
    while A[1] >= fat:
        p1 = p1 - 1
        A[1] = A[1] - fat
        fat = fat + 1

    p2 = p2 - A[1]
    for i in range(1, A[0] + 1):
        if i == p1 or i == p2:
            print('b', end='')
        else:
            print('a', end='')
    print('')


T = int(input())
for i in range(T):
    solve()
