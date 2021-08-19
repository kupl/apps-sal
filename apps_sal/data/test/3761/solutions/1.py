import sys
sys.setrecursionlimit(8001)
s = input()
X, Y = map(int, input().split())
S = list(map(len, s.split('T')))
N = len(S)
# if N == 1:
#   print(['No', 'Yes'][X == S[0] and Y == 0])
#   return
# elif N == 2:
#   print(['No', 'Yes'][X == S[0] and abs(Y) == S[1]])
#   return

x = S[0]
y = 0
xmoves = S[2::2]
xmoves.sort()
xmoves.reverse()
ymoves = S[1::2]
ymoves.sort()
ymoves.reverse()


def process(a, l, i, v, d, memo, r):
    if (i, v) in memo:
        return False
    if l == i:
        return v == d
    ab = abs(d - v)
    if ab > r:
        ret = False
    elif a == r:
        ret = True
    else:
        ret = process(a, l, i + 1, v + a[i], d, memo, r - a[i]) or process(a, l, i + 1, v - a[i], d, memo, r - a[i])
    memo[(i, v)] = ret
    return ret


if process(xmoves, len(xmoves), 0, x, X, {}, sum(xmoves)) and process(ymoves, len(ymoves), 0, y, Y, {}, sum(ymoves)):
    print('Yes')
else:
    print('No')
