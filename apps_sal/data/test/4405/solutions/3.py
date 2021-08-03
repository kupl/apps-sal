# from collections import Counter as C
# n, k_ = map(int, input().split())
# l = [*map(int, input().split())]

# c = C(l)
# d = {}
# for k, v in c.items():
#     d[v] = d.get(v, []) + [str(k)]

# ld = sorted([(k, v) for k, v in d.items()], reverse = True)

# res = []
# # print(ld)
# for e in ld:
#     res += [e[1]]
#     if e[0] * len(res) >= k_:
#         i = 0
#         while k_ > e[0] * len(res[i]):
#             print((' '.join(res[i]) + ' ') * e[0])
#             i += 1
#             k_ -= e[0] * len(res[i])
#         # if k_:
#         #     print((res[i] + ' ') * k_)
#         return


from bisect import bisect_left, bisect_right
from collections import Counter as C

n_ = int(input())
l = sorted(C(map(int, input().split())).values())
n = len(l)
i = res = 0

# print(l)


def f(x):
    i = 0
    for m in range(33):
        t = x << m
        i = bisect_left(l, t, i)
        if i == n:
            return t - x
        i += 1


res = 0
for x in range(1, n_ + 1):
    res = max(res, f(x))

print(res)
