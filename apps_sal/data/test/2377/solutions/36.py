N, H = map(int, input().split())
A = []
B = []
for i in range(N):
    AB = list(map(int, input().split()))
    A.append(AB[0])
    B.append(AB[1])

B.sort(reverse=True)
Amax = max(A)
ans = 0

for i in range(N):
    if B[i] < Amax:
        break

    H -= B[i]
    ans += 1
    if H <= 0:
        break

if H > 0:
    ans = ans + (-(-H // Amax))

print(ans)
