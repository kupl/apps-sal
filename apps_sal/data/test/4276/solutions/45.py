N, T = list(map(int, input().split()))
ans = float("inf")
for i in range(N):
    a, b = map(int, input().split())
    if T >= b:
        ans = min(ans, a)
print("TLE" if ans == float("inf") else ans)
