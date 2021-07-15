N = int(input())
T = list(map(int, input().split()))
V = list(map(int, input().split()))

MAX_V = [0]
for t, v in zip(T, V):
    MAX_V[-1] = min(MAX_V[-1], v)
    MAX_V.extend([v] * (2 * t))

REAL_V = [0]
for i in range(len(MAX_V) - 1):
    REAL_V.append(min(REAL_V[-1] + 0.5, MAX_V[i + 1]))

REAL_V[-1] = 0
for i in reversed(list(range(len(MAX_V) - 1))):
    REAL_V[i] = min(REAL_V[i], REAL_V[i + 1] + 0.5, MAX_V[i])

ans = 0
for i in range(len(MAX_V) - 1):
    ans += ((REAL_V[i] + REAL_V[i + 1]) * 0.5) / 2
print(ans)

