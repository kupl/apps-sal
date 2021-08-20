def read_ints():
    return list(map(int, input().strip().split()))


(t, k) = read_ints()
all = []
for _ in range(k):
    avail = list(read_ints())
    for x in avail[1:]:
        all.append(x)
all.sort()
(res_min, res_max) = (0, 0)
last = 0
for num in all:
    d = num - last
    res_min += d // 2
    res_max += d - 1
    last = num
d = t - last
res_min += d // 2
res_max += d - 1
print(res_min, res_max)
