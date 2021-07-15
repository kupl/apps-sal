from bisect import insort

tot, wr, ma, mas, mis = map(int, input().split())
s = sorted(map(int, input().split()))
res = []
while wr < tot:
    if not s or (s[wr // 2] < mis or s[wr // 2 - 1] < mis):
        res.append(mis)
        insort(s, mis)
    else:
        res.append(1)
        insort(s, 1)
    wr += 1
if sum(s) <= mas and s[tot // 2] >= mis:
    print(' '.join(map(str, res)))
else:
    print(-1)
