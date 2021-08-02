from sys import stdin

input = stdin.readline
#
# m, n, k, t = map(int, input().split())
#
# a = list(map(int, input().split()))
#
# t -= n
# mxr = [0] * (n+2)
# mxl = [0] * (n+2)
#
# trapr = [0] * (n+2)
# trapl = [0] * (n+2)
# for i in range(k):
#     l, r, d = map(int, input().split())
#     trapr[r] = max(trapr[r], d)
#     trapl[l] = max(trapl[l], d)
#
# for i in range(n+1)[::-1]:
#     mxr[i] = max(mxr[i + 1], trapr[i])
#
# for i in range(1, n+1):
#     mxl[i] = max(mxl[i - 1], trapl[i])
#
# ans = 0
# a.sort()
# from bisect import *
#
# for i in range(n+1):
#     f = i + t // 2
#     f = min(f, n)
#     mx = max(mxl[i], mxr[f + 1])
#     # print(n, m-bisect_left(a, mx))
#     ans = max(ans, m - bisect_left(a, mx))
#     # print(i, f, mx, ans)
#
# print(ans)
#
# trap = []
#
#
# def check(x):
#     avg = a[-x]
#     cost = n+1
#     nr = 0
#     for i in range(k):
#         xx, y, d = trap[i]
#         # print(avg,xx, y, d, cost,nr)
#         if d <= avg:
#             continue
#         if y > nr:
#             # print('1')
#             cost += (y - max(xx - 1, nr)) * 2
#             # print(xx,y,d,cost)
#             nr = y
#      # print(x, cost)
#     return cost <= t
#
#
# for i in range(k):
#     trap.append(list(map(int, input().split())))
#
# trap.sort()
#
# l = 0
# r = m+1
#
# while r - l > 1:
#     mid = (l + r) // 2
#     # print(mid)
#     if check(mid):
#         l = mid
#     else:
#         r = mid
#
#
# print(l)


def works(mid):
    ag = A[-mid]
    MAX = 0
    cur = 0
    out = N + 1
    for l, r, d in traps:
        if d <= ag:
            continue
        if r > MAX:
            out += (r - max(l - 1, MAX)) * 2
            MAX = r
        # if l > MAX:
        #     out += (MAX-cur)*2
        #     MAX,cur = r,l-1
        # else:
        #     MAX = max(MAX,r)
    return out <= time


S, N, T, time = map(int, input().split())
A = list(map(int, input().split()))
traps = [tuple(map(int, input().split())) for _ in range(T)]
traps.sort()
# traps.append((N+2,N+5,10**6))
A.sort()


lo = 0  # works
hi = S + 1  # does not work
while hi - lo > 1:
    mid = (hi + lo) // 2
    if works(mid):
        lo = mid
    else:
        hi = mid

print(lo)
