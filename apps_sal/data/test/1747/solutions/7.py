n = input()
p = input()
n = n.split(' ')
k = int(n[1])
n = int(n[0])
p = p.split(' ')
p = [int(q) for q in p]
cnt = [0 for i in range(0, int(1000000.0 + 1))]
curcnt = 0
l = 0
r = -1
maxlen = -1
maxl = 0
maxr = 0
while r < n - 1 and l <= n:
    while r < n - 1 and curcnt + (cnt[p[r + 1]] == 0) <= k:
        curcnt = curcnt + (cnt[p[r + 1]] == 0)
        cnt[p[r + 1]] += 1
        r += 1
    if maxlen < r - l:
        maxlen = r - l
        maxr = r
        maxl = l
    cnt[p[l]] -= 1
    curcnt -= cnt[p[l]] == 0
    l += 1
print(str(maxl + 1) + ' ' + str(maxr + 1))
