import sys
sys.setrecursionlimit(100000000)
# def input(): return sys.stdin.readline()[:-1]
def iin(): return int(input())
def impin(): return list(map(int, input().split()))
def irrin(): return [int(x) for x in input().split()]
def imrin(n): return [int(input()) for _ in range(n)]


def c(n, k):
    if n < k:
        return 0
    s = 1
    for i in range(1, k + 1):
        s *= n - i + 1
        s //= i
    return s


n, x, k = impin()
arr = irrin()
if k == 0:
    trr = {}
    frr = {}
    for a in arr:
        if a % x != 0:
            p = a // x
            if p in trr:
                trr[p] += 1
            else:
                trr[p] = 1
            if a in frr:
                frr[a] += 1
            else:
                frr[a] = 1
    s = 0
    # print(trr)
    for p in trr:
        s += c(trr[p] + 1, 2)
        # print(trr[p], s)
    for a in frr:
        s += c(frr[a], 2)
    print(s)
else:
    urr = {}
    lrr = {}
    for a in arr:
        u = (a - 1) // x + 1
        l = a // x
        # print(a, u, l)
        if u in urr:
            urr[u] += 1
        else:
            urr[u] = 1
        if l in lrr:
            lrr[l] += 1
        else:
            lrr[l] = 1
    s = 0
    for u in urr:
        # print(urr[u])
        l = u + k - 1
        # print(u, l)
        if l in lrr:
            s += urr[u] * lrr[l]
    print(s)


# s = 0
# for i in range(n):
#     for j in range(n):
#         if arr[i]>arr[j]:
#             continue
#         c = 0
#         for y in range(arr[i], arr[j]+1):
#             if y%x==0:
#                 c += 1
#         if c==k:
#             print(arr[i], arr[j])
#             s += 1
# print(s)
