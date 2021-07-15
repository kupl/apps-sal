M = 2 * 3 * 5 * 7
v = [0] * M
for i in range(1, M):
    v[i] = v[i - 1] + bool(i % 2 and i % 3 and i % 5 and i % 7)
n = int(input())
print(n // M * v[-1] + v[n % M])
