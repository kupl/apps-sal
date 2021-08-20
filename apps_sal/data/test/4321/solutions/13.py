import sys
input = sys.stdin.readline
(N, K) = map(int, input().split())
for _ in range(K):
    if N % 10 == 0:
        N //= 10
    else:
        N -= 1
print(N)
