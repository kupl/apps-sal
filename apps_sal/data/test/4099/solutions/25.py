n, k, m = map(int, input().split())
a = n * m - sum(map(int, input().split()))
print([0, [-1, a][a <= k]][a >= 0])
