N, K = list(map(int, input().split()))


def sub_sum(l, r):
    return (l + r) * (r - l + 1) / 2


ans = 0

for i in range(K, N + 2):
    l = sub_sum(0, i - 1)
    r = sub_sum(N - i + 1, N)
    ans += r - l + 1

ans = ans % (10**9 + 7)

print((int(ans)))
