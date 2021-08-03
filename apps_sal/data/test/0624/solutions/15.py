import sys
n, k, m = [int(i) for i in input().split(' ')]
#
# def helper(pows, k, m):
#     res = -sys.maxsize
#     def dfs(cur, cur_o, sums, sum_o):
#         if sum_o >= m:
#             return
#         for i, num in enumerate(cur):
#             dfs(cur)


def helper(pows, k, m):
    res = -sys.maxsize
    pref = [0]
    for i in range(len(pows)):
        pref.append(pref[-1] + pows[i])
    # print(pref)
    if len(pows) == 1:
        return pows[0] + k
    for i in range(min(len(pows), m + 1)):
        total = m - i
        if ((len(pows) - i) * k) <= total:
            res = max(res, (pref[-1] - pref[i] + ((len(pows) - i) * k)) / (len(pows) - i))
        else:
            res = max(res, (pref[-1] - pref[i] + total) / (len(pows) - i))
        # print(res, i)
    return res


pows = [int(i) for i in input().split(' ')]
pows.sort()
print(helper(pows, k, m))
