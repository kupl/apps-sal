import sys
input = sys.stdin.readline
(N, K) = list(map(int, input().split()))
if K % 2 == 0:
    A = list(range(K // 2, N + 1, K))
    B = list(range(K, N + 1, K))
else:
    A = list(range(K, N + 1, K))
    B = []
print(len(A) ** 3 + len(B) ** 3)
