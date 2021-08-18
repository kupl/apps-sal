n, m = map(int, input().split())
xl = sorted(list(map(int, input().split())))

diff = [0] * (m - 1)

for i in range(m - 1):
    diff[i] = xl[i + 1] - xl[i]

diff_s = sorted(diff, reverse=True)
print(sum(diff_s[n - 1:]))
