N = int(input())
M = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
imp = fuel = 0
for i in range(N, 0, -1):
    if i == N:
        i = 0
    if B[i] == 1:
        imp = 1
        break
    fuel += (M + fuel) / (B[i] - 1)
    if A[i - 1] == 1:
        imp = 1
        break
    fuel += (M + fuel) / (A[i - 1] - 1)
print(-1 if imp else '{:.7f}'.format(fuel))
