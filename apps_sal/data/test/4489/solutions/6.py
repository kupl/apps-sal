n = int(input())
sl = list(input() for _ in range(n))
m = int(input())
tl = list(input() for _ in range(m))

sl_s = list(set(sl))
tl_s = list(set(tl))

ans = 0
for s in sl_s:
    ans = max(ans, sl.count(s) - tl.count(s))

print(ans)
