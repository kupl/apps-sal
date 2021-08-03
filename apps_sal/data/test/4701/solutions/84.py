N = int(input())
K = int(input())
x = 1
for _ in range(N):
    x = min(x * 2, x + K)
print(x)
