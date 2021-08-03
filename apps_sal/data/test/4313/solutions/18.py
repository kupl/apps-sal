N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
for i in range(N):
    x = V[i] - C[i]
    if x > 0:
        ans += x
print(ans)
