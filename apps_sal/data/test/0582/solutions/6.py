# n = int(input())
# a = [int(i) for i in input().split(' ')]
# t = [int(i) for i in input().split(' ')]
#
# import collections
# from heapq import heapify, heappop, heappush
#
#
# l = collections.defaultdict(list)
# at = [[a[i], t[i]] for i in range(n)]
# at.sort(key = lambda x: x[0])
# for aa, tt in at:
#     l[aa].append(tt)
#
# for k in l.keys():
#     heapify(l[k])
#
#
# # print(at)
# # print(l)
# res = 0
#
# # tmp = []
#
# q = sorted(l.keys())[::-1]
# while q:
#     i = q.pop()
#     # print("i", i, l[i])
#     # l[i].extend(tmp)
#     if len(l[i]) == 1:
#         continue
#     else:
#         tmp = sorted(l[i])
#         sums = sum(tmp)
#         # res += sums - maxx # leave the one with max time and increase all other by 1, cost their time
#         idx = i
#         while tmp and ((q and idx + 1 != q[-1]) or not q):
#             # print(i, idx, q, tmp)
#             p = tmp.pop()
#             res += sums - p
#             sums -= p
#             idx += 1
#         if tmp:
#             p = tmp.pop()
#             res += sums - p
#             sums -= p
#             l[idx+1].extend(tmp)
#             if not q:
#                 q.append(idx+1)
# print(res)
#
#
#
#
#
#
#


import sys

inp = sys.stdin.readline
def input(): return inp().strip()


# flush= sys.stdout.flush
# import threading
# sys.setrecursionlimit(10**6)
# threading.stack_size(2**26)

def iin(): return int(input())


def lin(): return list(map(int, input().split()))


def main():
    import heapq as hq
    n = iin()
    a = lin()
    t = lin()
    dc = {}
    for i in range(n):
        try:
            dc[a[i]].append(t[i])
        except:
            dc[a[i]] = [t[i], ]
    # print(dc)
    sa = list(dc.keys())
    sa.sort()
    n = len(sa)
    ch = 0
    pt = sa[ch]
    temp = []
    sm = 0
    ans = 0
    hq.heapify(temp)
    done = 0
    while ch < n:
        # print(temp, sa[ch])
        pt = sa[ch]
        if len(dc[pt]) > 1 or done:
            a1 = sorted(dc[pt])
            for item in a1:
                hq.heappush(temp, -item)
                sm += item
            x = hq.heappop(temp) * (-1)
            dc[pt] = [x]
            sm -= x
            while len(temp):
                # print('A', ch, pt, temp )
                ans += sm
                pt += 1
                if pt in dc:
                    ch += 1
                    done = 1
                    break
                else:
                    x = hq.heappop(temp) * (-1)
                    sm -= x
            else:
                done = 0
        else:
            ch += 1
            done = 0
    # print(dc)
    print(ans)


main()
