import sys
input = sys.stdin.readline
n, c = list(map(int, input().strip().split()))

a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

stairs = [0 for _ in range(n)]
elevator = [0 for _ in range(n)]
elevator[0] = c

for i in range(1, n):
    stairs[i] = min(elevator[i - 1], stairs[i - 1]) + a[i - 1]
    elevator[i] = min(elevator[i - 1], stairs[i - 1] + c) + b[i - 1]
print(' '.join(str(min(elevator[i], stairs[i])) for i in range(n)))
