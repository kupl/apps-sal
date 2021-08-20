N = int(input())
A = list(map(int, input().split()))
now = 0
ans = 0
for i in range(N):
    if A[i] == now + 1:
        now += 1
    else:
        ans += 1
if ans == N:
    print(-1)
else:
    print(ans)
