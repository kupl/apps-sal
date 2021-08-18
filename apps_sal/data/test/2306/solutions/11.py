import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

N = int(input())
T = [0] + list(map(int, input().split()))
V = [0] + list(map(int, input().split()))

left = [0] * (N + 1)
right = [0] * (N + 1)

for i in range(1, N):
    start = left[i - 1]
    left[i] = min(start + T[i], V[i], V[i + 1])

for i in range(N - 1, 0, -1):
    start = right[i + 1]
    right[i] = min(start + T[i + 1], V[i], V[i + 1])

total = [min(left[i], right[i]) for i in range(N + 1)]
ans = 0
for i in range(1, N + 1):
    x = (V[i] - total[i - 1]) + (V[i] - total[i])
    if x >= T[i]:
        V[i] = (total[i - 1] + T[i] + total[i]) / 2
        x = T[i]
    d = (total[i - 1] + V[i]) * (V[i] - total[i - 1]) / 2
    d += (total[i] + V[i]) * (V[i] - total[i]) / 2
    d += V[i] * (T[i] - x)

    ans += d

print(ans)
