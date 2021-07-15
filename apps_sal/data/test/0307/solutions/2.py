read = lambda: list(map(int, input().split()))
k2, k3, k5, k6 = read()
cnt1 = min(k2, k5, k6)
cnt2 = min(k2 - cnt1, k3)
ans = cnt1 * 256 + cnt2 * 32
print(ans)

