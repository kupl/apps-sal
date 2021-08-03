hh, mm = list(map(int, input().split(':')))

ans = 0
for i in range(1440):
    t = hh * 60 + mm + i
    hi = str((t // 60) % 24)
    if len(hi) == 1:
        hi = '0' + hi
    mi = str(t % 60)
    if len(mi) == 1:
        mi = '0' + mi
    s = hi + ':' + mi
    if list(s) == list(reversed(list(s))):
        ans = i
        break

print(ans)
