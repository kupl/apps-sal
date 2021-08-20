from math import ceil
T = int(input())
for _ in range(T):
    (N, D) = list(map(int, input().split()))

    def calc(D, x):
        return x + ceil(D / (x + 1))
    for i in range(N):
        if calc(D, i) <= N:
            print('YES')
            break
    else:
        print('NO')
