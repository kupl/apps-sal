from bisect import bisect_left

n, k = list(map(int, input().split()))
x = list(map(int, input().split()))

pos = bisect_left(x, 0)
if pos < len(x) and x[pos] == 0:
    k -= 1
else:
    x.insert(pos, 0)

l = pos
r = pos + k

if r >= len(x):
    diff = r - len(x) + 1
    l -= diff
    r -= diff

ans = min(abs(x[l]), x[r]) * 2 + max(abs(x[l]), x[r])

while r >= pos:
    if l < 0:
        break

    dist = min(abs(x[l]), x[r]) * 2 + max(abs(x[l]), x[r])
    if dist < ans:
        ans = dist

    l -= 1
    r -= 1

print(ans)
