N = int(input())
A = list(map(int, input().split()))
start = [0] * N
ans = 0
for i in range(N):
    if i + A[i] + 1 < N:
        start[i + A[i] + 1] += 1

for i in range(N):
    if i - A[i] + 1 < 0:
        continue
    if i - A[i] + 1 >= N:
        continue
    ans += start[i - A[i] + 1]

print(ans)
