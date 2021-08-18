def solve(A, ans):
    for x in [x - ans for x in A]:
        ans += x // 3
    return ans


A = [int(x) for x in input().split()]
m = min(A)
ans = solve(A, m)
if m:
    ans = max(ans, solve(A, m - 1))
print(ans)
