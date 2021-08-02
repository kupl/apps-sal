N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ame_A = [0] * N
ame_B = [0] * N

for i in range(N):
    if i == 0:
        ame_A[i] += A[i]
        continue
    ame_A[i] += ame_A[i - 1] + A[i]

for i in range(N - 1, -1, -1):
    if i == N - 1:
        ame_B[i] += B[i]
        continue
    ame_B[i] += ame_B[i + 1] + B[i]

ans = 0
for j in range(N):
    cnt = ame_A[j] + ame_B[j]
    ans = max(ans, cnt)

print(ans)
