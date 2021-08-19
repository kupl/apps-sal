__author__ = 'Andrey'
(n, w) = map(int, input().split())
volumes = list(map(int, input().split()))
volumes.sort()
m = -1
if volumes[0] * 2 <= volumes[n]:
    possible = 3 * n * volumes[0]
    if possible <= w:
        m = max(m, possible)
if volumes[n] / 2 <= volumes[0]:
    possible = volumes[n] / 2 * 3 * n
    if possible <= w:
        m = max(m, possible)
if w / (3 * n) <= volumes[0] and 2 * w / (3 * n) <= volumes[n]:
    m = max(m, w)
print(m)
