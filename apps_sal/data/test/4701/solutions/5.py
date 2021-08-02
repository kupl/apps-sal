N = int(input())
K = int(input())

start = 1

for n in range(N):
    start = min(start * 2, start + K)

print(start)
