(n, k) = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
cands = []
for x in range(1, int(s ** 0.5) + 1):
    if s % x == 0:
        cands.append(x)
        if x != s // x:
            cands.append(s // x)
cands.sort(reverse=True)
ans = 0
for cand in cands:
    b = [a[i] % cand for i in range(n)]
    b.sort()
    sb = [0 for _ in range(n + 1)]
    for i in range(n):
        sb[i + 1] = sb[i] + b[i]
    flg = False
    for i in range(n + 1):
        x = max(sb[i], cand * (n - i) - (sb[n] - sb[i]))
        if x <= k:
            flg = True
            break
    if flg:
        print(cand)
        break
