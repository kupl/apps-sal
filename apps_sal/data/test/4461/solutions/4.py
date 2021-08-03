h, w = map(int, input().split())

tmps = 0
ans = 10**18
for i in range(1, h):
    k = (h - i) // 2
    t = [i * w, k * w, (h - i - k) * w]
    tmp = max(t) - min(t)
    ans = min(tmp, ans)
    k = w // 2
    t = [i * w, (h - i) * k, (h - i) * (w - k)]
    tmp = max(t) - min(t)
    ans = min(tmp, ans)
for i in range(1, w):
    k = (w - i) // 2
    t = [i * h, k * h, (w - i - k) * h]
    tmp = max(t) - min(t)
    ans = min(tmp, ans)
    k = h // 2
    t = [i * h, (w - i) * k, (w - i) * (h - k)]
    tmp = max(t) - min(t)
    ans = min(tmp, ans)
print(ans)
