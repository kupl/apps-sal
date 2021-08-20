from collections import defaultdict
N = int(input())
S = input()
T = S[::-1]
dic = defaultdict(lambda: [])
for (i, t) in enumerate(T):
    dic[t].append(i)
for k in list(dic.keys()):
    dic[k].reverse()
arr = []
for c in S:
    arr.append(dic[c].pop())


def inversion(inds):
    bit = [0] * (N + 1)

    def bit_add(x, w):
        while x <= N:
            bit[x] += w
            x += x & -x

    def bit_sum(x):
        ret = 0
        while x > 0:
            ret += bit[x]
            x -= x & -x
        return ret
    inv = 0
    for ind in reversed(inds):
        inv += bit_sum(ind + 1)
        bit_add(ind + 1, 1)
    return inv


print(inversion(arr))
