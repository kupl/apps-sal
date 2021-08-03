N, K = list(map(int, input().split()))

ans = 0
x = 1

while x <= N:
    x *= K
    ans += 1

print(ans)
