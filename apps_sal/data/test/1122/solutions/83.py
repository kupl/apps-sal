import sys
readline = sys.stdin.readline
(n, m) = map(int, readline().split())
l = 1
r = n
used = set()
while len(used) < m * 2:
    diff = r - l
    rdiff = n - diff
    if diff == rdiff:
        r -= 1
        continue
    if diff in used:
        r -= 1
        continue
    print(l, r)
    used.add(diff)
    used.add(rdiff)
    l += 1
    r -= 1
