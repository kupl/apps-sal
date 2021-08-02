N = int(input())
K = int(input())
x = 1
for _ in range(N):
    x = min(2 * x, x + K)
print(x)
