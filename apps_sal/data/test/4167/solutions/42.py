N, K = list(map(int, input().split()))


if (K % 2 != 0):
    ans = (N // K)**3
else:
    k = N // K
    k_ = N // (K // 2)
    ans = k**3 + (k_ - k)**3

print(ans)
