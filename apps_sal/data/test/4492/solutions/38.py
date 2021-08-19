(N, M) = map(int, input().split())
L = list(map(int, input().split()))
count = 0
if L[0] > M:
    count += L[0] - M
    L[0] -= L[0] - M
for i in range(1, N):
    if L[i] + L[i - 1] > M:
        count += L[i] + L[i - 1] - M
        L[i] -= L[i] + L[i - 1] - M
print(count)
