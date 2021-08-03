K, N = map(int, input().split())
A = list(map(int, input().split()))

max_d = 0

for a in range(1, N):
    d = A[a] - A[a - 1]
    if d > max_d:
        max_d = d
last_d = K - A[-1] + A[0]
if last_d > max_d:
    max_d = last_d
print(K - max_d)
