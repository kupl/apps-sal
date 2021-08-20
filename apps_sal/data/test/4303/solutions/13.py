from bisect import bisect_left
import sys
input = sys.stdin.readline
(N, K) = map(int, input().split())
x = list(map(int, input().split()))
x_shift = [i + abs(x[0]) for i in x]
dist = []
for i in range(N - K + 1):
    d_end = x_shift[i + K - 1] - x_shift[i]
    d_left = abs(x[i])
    d_right = abs(x[i + K - 1])
    dist.append(d_end + min(d_left, d_right))
print(min(dist))
