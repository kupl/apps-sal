n, k = (int(x) for x in input().split())
val = -10 ** 9
for i in range(n):
    f, t = (int(x) for x in input().split())
    cur = min(f, f - (t - k))
    if cur > val:
        val = cur
print(val)

