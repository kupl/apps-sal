from bisect import bisect_left, bisect_right

n, k = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
cuma = [0]
for i in range(1, n + 1):
    cuma.append(cuma[i - 1] + a[i])

if cuma[-1] < k: print((0)); return
r = bisect_left(cuma, k)

ans = 0
for i in range(r, len(cuma)):
    l = bisect_right(cuma, cuma[i] - k)
    ans += l

print(ans)
