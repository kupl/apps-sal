from collections import Counter
from bisect import bisect, bisect_left
n, k = map(int, input().split())
a = list(map(int, input().split()))
a = Counter(a)
c = sorted(Counter(a).items())
keys = sorted(Counter(a).keys())

m = len(c)
l_cum = [c[0][0] * c[0][1]]
l_cnt = [c[0][1]]
for i in range(1, m):
    l_cum.append(l_cum[-1] + c[i][0] * c[i][1])
    l_cnt.append(l_cnt[-1] + c[i][1])


r_cum = [0 for _ in range(m)]
r_cum[-1] = c[-1][0] * c[-1][1]
r_cnt = [0 for _ in range(m)]
r_cnt[-1] = c[-1][1]
for i in range(m - 2, -1, -1):
    r_cum[i] = r_cum[i + 1] + c[i][0] * c[i][1]
    r_cnt[i] = r_cnt[i + 1] + c[i][1]

# print(l_cum)
# print(r_cum)

ans = 10**20
for i in range(m):
    c_num = a[keys[i]]
    if c_num >= k:
        ans = 0
        break

    if i > 0:
        l_res = (keys[i] - 1) * l_cnt[i - 1] - l_cum[i - 1]
        l_num = l_cnt[i - 1]
    else:
        l_res = 10**30
        l_num = 0
    if i < m - 1:
        r_res = r_cum[i + 1] - (keys[i] + 1) * r_cnt[i + 1]
        r_num = r_cnt[i + 1]
    else:
        r_res = 10**30
        r_num = 0

    if c_num + l_num < k and c_num + r_num < k:
        ans = min(ans, l_res + r_res + k - c_num)
    elif c_num + l_num < k:
        ans = min(ans, r_res + k - c_num)
    elif c_num + r_num < k:
        ans = min(ans, l_res + k - c_num)
    else:
        ans = min(ans, min(r_res, l_res) + k - c_num)
    # print(ans)

print(ans)
