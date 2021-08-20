(N, D) = map(int, input().split())
ans = 0
while N > 0:
    N -= D * 2 + 1
    ans += 1
print(ans)
