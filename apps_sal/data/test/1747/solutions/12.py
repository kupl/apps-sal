def R(): return map(int, input().split())


n, k = R()
arr = list(R())
rl, rr = 0, 0
l = 0
rec = {}
for r, v in enumerate(arr):
    rec.setdefault(v, 0)
    rec[v] += 1
    while len(rec) > k:
        rec[arr[l]] -= 1
        if not rec[arr[l]]:
            rec.pop(arr[l])
        l += 1
    if rr - rl < r - l:
        rl, rr = l, r
print(rl + 1, rr + 1)
