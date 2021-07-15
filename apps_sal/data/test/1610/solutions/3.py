import sys

(n, k) = list(map(int, input().split()))

a = list(range(1, k+2))[::-1] + list(range(k+2, n+1))

print(*a)

