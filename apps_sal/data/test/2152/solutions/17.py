n = int(input())
ans = 0
curMin = 101
for i in range(n):
    a, p = list(map(int, input().strip().split()))
    curMin = min(p, curMin)
    ans += a * curMin

print(ans)
