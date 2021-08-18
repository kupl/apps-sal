l1, r1, l2, r2, k = list(map(int, input().split()))
if l1 > r2 or r1 < l2:
    print(0)
    return
ml = max(l1, l2)
mr = min(r1, r2)
delta = 1 if ml <= k <= mr else 0
print(abs(mr - ml) + 1 - delta)
