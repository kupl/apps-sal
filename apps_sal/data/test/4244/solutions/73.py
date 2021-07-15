N = int(input())
X = list(map(int, input().split()))

ans = 1e10
for p in range(max(X)+1):
    sum_power = 0
    for i in range(N):
        sum_power += (X[i]-p)**2
    if ans > sum_power:
        ans = sum_power

print(ans)
