N = int(input())
K = int(input())
start = 1
for i in range(N):
    start = min(start * 2, start + K)
print(str(start))
