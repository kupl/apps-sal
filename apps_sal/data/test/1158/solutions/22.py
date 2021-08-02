n, k = map(int, input().split())
M = list(map(int, input().split()))

T = [0] * 100
for i in range(n):
    T[M[i] - 1] += 1

t, b = 0, 0
for i in range(100):
    if T[i] != 0:
        t += 1
        b = max(b, (T[i] + k - 1) // k)

print(b * t * k - n)
