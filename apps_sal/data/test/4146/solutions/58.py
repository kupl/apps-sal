import sys
from collections import Counter
from operator import itemgetter
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (n, *V) = list(map(int, read().split()))
    counter1 = Counter(V[::2])
    counter2 = Counter(V[1::2])
    vec1 = sorted(list(counter1.items()), reverse=True, key=itemgetter(1))
    vec2 = sorted(list(counter2.items()), reverse=True, key=itemgetter(1))
    if vec1[0][0] != vec2[0][0]:
        ans = n - vec1[0][1] - vec2[0][1]
    elif len(vec1) == len(vec2) == 1:
        ans = n // 2
    else:
        tmp = []
        if len(vec1) > 1:
            tmp.append(vec1[1][1] + vec2[0][1])
        if len(vec2) > 1:
            tmp.append(vec1[0][1] + vec2[1][1])
        ans = n - max(tmp)
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
