n = int(input())
a = [int(x) for x in input().split()]
m = len(a)
sums = [0] * (m + 1)
count = 0
a.insert(0, 0)
add = 0
for i in range(m // 2 - 1, -1, -1):
    m = max(a[2 * i + 1], a[2 * i + 2])
    need_l = m - a[2 * i + 1]
    need_r = m - a[2 * i + 2]
    add += need_l + need_r
    a[i] += a[2 * i + 1] + need_l
print(add)
