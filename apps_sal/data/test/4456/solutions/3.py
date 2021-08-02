from heapq import *


def solve(a, b):

    b_map = {i: idx for idx, i in enumerate(a)}

    intervals = []

    for idx, i in enumerate(b):
        f = b_map[i]
        intervals.append(sorted([f, idx]))

    intervals.sort(reverse=True)
    res = []
    endings = []
    for i in range(len(a)):
        while endings and endings[0] < i:
            heappop(endings)

        if not res:
            res.append(97)
        elif not endings:
            res.append(res[-1] + 1)
        else:
            res.append(res[-1])

        while intervals and intervals[-1][0] <= i:
            s, e = intervals.pop()
            heappush(endings, e)

    def build(k, r):
        res = [0] * len(k)

        for idx, i in enumerate(k):

            res[i - 1] = r[idx]

        return res
    # print(res)
    return build(a, res)


n, k = [int(i) for i in input().split()]

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

b = solve(a, b)
string = ''.join(chr(min(i, 97 + 25)) for i in b)
if len(set(string)) < k:
    print("NO")
else:
    print("YES")
    print(string)
