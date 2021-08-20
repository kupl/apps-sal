import math
(n, h, k) = (int(i) for i in input().split())
l = list(map(int, input().split()))
ans = 0
i = 0
dh = 0
while i < n:
    if dh + l[i] <= h:
        dh += l[i]
        i += 1
    else:
        ans += math.ceil((l[i] - (h - dh)) / k)
        dh = max(dh - k * math.ceil((l[i] - (h - dh)) / k), 0)
ans += math.ceil(dh / k)
print(ans)
