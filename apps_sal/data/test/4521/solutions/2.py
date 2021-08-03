import sys
input = sys.stdin.readline

n = int(input())
X = list(map(int, input().split()))
V = list(map(int, input().split()))

XV = [(X[i], V[i]) for i in range(n)]

#compression_dict_x={a: ind for ind, a in enumerate(sorted(set(X)))}
compression_dict_v = {a: ind + 2 for ind, a in enumerate(sorted(set(V)))}

XV = [(XV[i][0], compression_dict_v[XV[i][1]]) for i in range(n)]
XV.sort(reverse=True)

LEN = len(compression_dict_v) + 3

BIT1 = [0] * (LEN + 1)


def update1(v, w):
    while v <= LEN:
        BIT1[v] += w
        v += (v & (-v))


def getvalue1(v):
    ANS = 0
    while v != 0:
        ANS += BIT1[v]
        v -= (v & (-v))
    return ANS


BIT2 = [0] * (LEN + 1)


def update2(v, w):
    while v <= LEN:
        BIT2[v] += w
        v += (v & (-v))


def getvalue2(v):
    ANS = 0
    while v != 0:
        ANS += BIT2[v]
        v -= (v & (-v))
    return ANS


ANS = 0
for x, v in XV:
    ANS += (getvalue2(LEN) - getvalue2(v - 1)) - (getvalue1(LEN) - getvalue1(v - 1)) * x
    # print(getvalue2(LEN),getvalue2(v-1),getvalue1(LEN),getvalue1(v-1))
    # print(x,v,ANS)

    update1(v, 1)
    update2(v, x)

print(ANS)
