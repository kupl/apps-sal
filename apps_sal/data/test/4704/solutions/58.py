N = int(input())
A = list(map(int, input().split()))

sunuke = [0] * (N)
guma = [0] * (N)

for i in range(N - 1):
    if i == 0:
        sunuke[i] += A[i]
        continue
    sunuke[i] += sunuke[i - 1] + A[i]

for j in range(N - 1, 0, -1):
    if j == N - 1:
        guma[j] += A[j]
        continue
    guma[j] += guma[j + 1] + A[j]

ans = float("inf")
for k in range(N - 1):
    ans = min(ans, abs(sunuke[k] - guma[k + 1]))

print(ans)
