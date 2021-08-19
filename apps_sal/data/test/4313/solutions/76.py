N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
for i in range(N):
    tmp = V[i] - C[i]
    if tmp > 0:
        ans += tmp
print(ans)
