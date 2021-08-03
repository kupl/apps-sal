def Game(n, k):
    if k % 3 != 0:
        return [1, 0, 0][n % 3]
    else:
        n %= (k + 4)
        if n == k + 3:
            return 0
        else:
            return [1, 0, 0][n % 3]


for i in range(int(input())):
    N, K = list(map(int, input().split()))
    print(['Alice', 'Bob'][Game(N, K - 3)])
