N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
for i in range(N):
    sa = V[i] - C[i]
    if sa > 0:
        ans += sa
print(ans)
