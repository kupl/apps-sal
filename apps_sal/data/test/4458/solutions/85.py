n = int(input())
P = list(map(int, input().split()))
ans = 0
m = 200002
for p in P:
    if p <= m:
        m = p
        ans += 1
print(ans)
