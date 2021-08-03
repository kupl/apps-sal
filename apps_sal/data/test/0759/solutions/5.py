from math import ceil
h, m = list(map(int, input().split()))
H, D, C, N = list(map(int, input().split()))

diff = max(0, 20 * 60 - (h * 60 + m))

ans = min(ceil(H / N) * C, ceil((H + diff * D) / N) * 0.8 * C)

print(ans)
