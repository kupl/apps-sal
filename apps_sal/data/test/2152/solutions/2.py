n = int(input())
ans = 0
minp = 10**10
for i in range(n):
    a, p = list(map(int, input().split()))
    if p < minp:
        minp = p
    ans += a * minp
print(ans)
