import heapq
import sys
input = sys.stdin.readline
(n, k) = list(map(int, input().split()))
S = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]
S.sort()
segtemp = 2 * 10 ** 5
seg_el = 1 << segtemp.bit_length()
SEG = [0] * (2 * seg_el)


def getvalue(n, seg_el):
    i = n + seg_el
    ANS = 0
    ANS += SEG[i]
    i >>= 1
    while i != 0:
        ANS += SEG[i]
        i >>= 1
    return ANS


def updates(l, r, x):
    L = l + seg_el
    R = r + seg_el
    while L < R:
        if L & 1:
            SEG[L] += x
            L += 1
        if R & 1:
            R -= 1
            SEG[R] += x
        L >>= 1
        R >>= 1


ind = 0
SH = []
ANS = []
for point in range(segtemp):
    while ind < n and S[ind][0] <= point:
        (l, r, x) = S[ind]
        updates(l, r + 1, 1)
        ind += 1
        heapq.heappush(SH, (-r, l, x))
    while getvalue(point, seg_el) > k:
        (r, l, x) = heapq.heappop(SH)
        r = -r
        ANS.append(x)
        updates(l, r + 1, -1)
print(len(ANS))
print(*ANS)
