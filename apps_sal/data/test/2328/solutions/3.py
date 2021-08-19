import sys
input = sys.stdin.readline
Query = int(input())
for query in range(Query):
    (n, k) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()
    L = 10 ** 15
    for i in range(k, n):
        if A[i] - A[i - k] < L:
            L = A[i] - A[i - k]
            ANS = (A[i] + A[i - k]) // 2
    print(ANS)
