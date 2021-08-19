n = int(input())
p = list(map(int, input().split()))
r = 0
ans = 0
while r < n:
    if p[r] == r + 1:
        ans += 1
        r += 1
    r += 1
print(ans)
