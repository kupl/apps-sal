N = int(input().strip())
A_list = list(map(int, input().rstrip().split()))
plus_h = {}
minus_h = {}
for i in range(N):
    p = i + 1 + A_list[i]
    m = i + 1 - A_list[i]
    plus_h.setdefault(p, 0)
    plus_h[p] += 1
    minus_h.setdefault(m, 0)
    minus_h[m] += 1
cnt = 0
for k in plus_h:
    if k in minus_h:
        cnt += plus_h[k] * minus_h[k]
print(cnt)
