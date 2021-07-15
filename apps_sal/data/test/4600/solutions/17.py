n, m = map(int, input().split())
ps = [list(input().split()) for _ in range(m)]
ans = [0]*n
wa = [0]*n
ac = [0]*n
for i in range(m):
    p, s = int(ps[i][0]), ps[i][1]
    if ac[p-1] == 0:
        if s == 'WA':
            wa[p-1] += 1
        else:
            ans[p-1] = wa[p-1]
            ac[p-1] += 1
print(sum(ac), sum(ans))
