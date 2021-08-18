N = int(input())
P = list(map(int, input().split()))
min_p = 10**10
ans = 0
for i in range(N):
    if min_p >= P[i]:
        ans += 1
    min_p = min(min_p, P[i])
print(ans)
