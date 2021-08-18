import sys
import itertools


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N, K = lr()
XY = [lr() for _ in range(N)]
XY.sort()
answer = float('inf')
for i, j in itertools.combinations(list(range(N)), 2):
    xleft = XY[i][0]
    xright = XY[j][0]
    candidate = sorted(XY[i:j + 1], key=lambda xy: xy[1])
    if len(candidate) < K:
        continue
    for s in range(len(candidate) - K + 1):
        yup = candidate[s + K - 1][1]
        ylow = candidate[s][1]
        area = (xright - xleft) * (yup - ylow)
        if area < answer:
            answer = area

print(answer)
