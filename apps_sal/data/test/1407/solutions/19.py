n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

isPrime = [False, False] + [True] * 101000
for i in range(2, len(isPrime)):
    if isPrime[i]:
        for j in range(i*i, len(isPrime), i):
            isPrime[j] = False

nextPrime = [0] * len(isPrime)
for i in range(len(isPrime) - 2, 0, -1):
    if isPrime[i]:
        nextPrime[i] = i
    else:
        nextPrime[i] = nextPrime[i+1]

row_scores = [0] * n
col_scores = [0] * m
for i in range(n):
    for j in range(m):
        row_scores[i] += nextPrime[a[i][j]] - a[i][j]
        col_scores[j] += nextPrime[a[i][j]] - a[i][j]
print(min(row_scores + col_scores))

