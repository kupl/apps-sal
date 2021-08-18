
n, m = list(map(int, input().split()))
h = list(map(int, input().split()))
ab = []
for i in range(m):
    ab.append(list(map(int, input().split())))

peak = [1] * n
for i in range(m):
    if h[ab[i][0] - 1] >= h[ab[i][1] - 1]:
        peak[ab[i][1] - 1] = 0
    if h[ab[i][0] - 1] <= h[ab[i][1] - 1]:
        peak[ab[i][0] - 1] = 0
print((sum(peak)))
