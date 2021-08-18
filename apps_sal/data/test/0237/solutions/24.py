n, m, k = list(map(int, input().split()))
p = m - n
min_d, max_d = min(abs(n - k + 1), k), max(abs(n - k + 1), k)
i = 1
r = m + 1
l = 0
while r - l > 1:
    i = (r + l) // 2
    min_dist = min_d - i
    max_dist = max_d - i
    min_summ = 0
    max_summ = 0
    if min_dist < 0:
        min_summ = (abs(min_dist) * (abs(min_dist) + 1))
    if max_dist < 0:
        max_summ = (abs(max_dist) * (abs(max_dist) + 1))
    summ = ((i * (i + 1)) - i) * 2 - min_summ - max_summ
    if summ > p * 2:
        r = i
    else:
        l = i

print(r)
