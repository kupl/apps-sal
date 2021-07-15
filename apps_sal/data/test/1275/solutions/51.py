N, K = map(int, input().split())
DN = 2 * N
ans = 0
for ab in range(2, DN + 1):
    cd = ab - K
    if cd < 2 or cd > DN:
        continue
    ans += min(DN - ab + 1, ab - 1) * min(DN - cd + 1, cd - 1)
print(ans)
