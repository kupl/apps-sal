import math

n, m = map(int, input().split(" "))
xL = sorted(list(map(int, input().split(" "))))

diff = [0 for _ in range(m - 1)]

for i in range(m - 1):
    diff[i] = xL[i + 1] - xL[i]

diff = sorted(diff, reverse=True)

print(sum(diff[n - 1:]))
