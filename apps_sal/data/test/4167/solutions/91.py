N, K = map(int, input().split())
if K % 2 == 1:
    ans = (N // K)**3
else:
    ans = (N // K)**3
    K2 = N // (K // 2) - N // K
    ans += K2**3
print(ans)
