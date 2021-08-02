n = int(input())
p = list(map(int, input().split()))
ans = 1
p_min = p[0]

for i in range(1, n):
    if p_min >= p[i]:
        ans += 1
    p_min = min(p_min, p[i])

print(ans)
