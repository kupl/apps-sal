n = int(input())
wl = list(map(int, input().split()))
sw = sum(wl)
ans, ww = 1001001001, 0
for w in wl:
    ww += w
    sw -= w
    ans = min(ans, abs(ww - sw))

print(ans)
