N = int(input())
a = [int(x) for x in input().split()]

M = max(a)

C = [0] * (M + 1)

for i in range(N):
    C[a[i]] += 1

ans = 0

for i in range(1, M):
    wa = C[i - 1] + C[i] + C[i + 1]
    ans = max(ans, wa)

if M <= 1:
    ans = N

print(ans)
