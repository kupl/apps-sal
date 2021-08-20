(card_num, gate_num) = map(int, input().split())
(lmax, rmin) = map(int, input().split())
for i in range(1, gate_num):
    (l, r) = map(int, input().split())
    lmax = max(lmax, l)
    rmin = min(rmin, r)
print(max(0, rmin - lmax + 1))
