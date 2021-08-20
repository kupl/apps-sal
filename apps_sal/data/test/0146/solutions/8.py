(n, k) = [int(v) for v in input().split()]
signs = [int(v) for v in input().split()]
tot_e = signs.count(1)
tot_s = signs.count(-1)
ans = 0
for b in range(k):
    (me, ms) = (0, 0)
    for c in range(b, n, k):
        if signs[c] == 1:
            me += 1
        else:
            ms += 1
    ans = max(ans, abs(tot_e - me - (tot_s - ms)))
print(ans)
