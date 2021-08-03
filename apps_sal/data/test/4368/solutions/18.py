N, K = map(int, input().split())
ans = 1
while N > 1:
    N = N // K
    ans += 1
if N % K == 0:
    ans -= 1
print(ans)
