N = int(input())
P = list(map(int, input().split()))
Pm = P[0]
ans = 0
for i in range(N):
    if P[i] <= Pm:
        ans += 1
        Pm = P[i]
print(ans)
