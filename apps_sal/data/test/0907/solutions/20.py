import sys
from collections import defaultdict
input = sys.stdin.readline


class Problem:
    def __init__(self):
        pass

    def solve(self):
        print(self._solve())

    def _solve(self):
        n, m = [int(item) for item in input().split()]
        pairs = []
        cnt = {}
        mp = defaultdict(int)
        for i in range(m):
            pair = sorted([int(item) for item in input().split()])
            pairs.append(pair)
            mp[pair[0]] += 1
            mp[pair[1]] += 1
            pair = tuple(pair)
            if pair in cnt:
                cnt[pair] += 1
            else:
                cnt[pair] = 1

        res = []

        for x in mp:
            res.append([mp[x], x])
        res.sort()
        for i in range(len(res) - 1, -1, -1):
            for j in range(len(res) - 1, i, -1):
                if res[i][0] + res[j][0] < m:
                    break
                pair = tuple(sorted([res[i][1], res[j][1]]))
                if pair[0] == pair[1]:
                    continue
                if not pair in cnt:
                    occs = 0
                else:
                    occs = cnt[pair]
                # print(pair, res[i][0], res[j][0], occs)
                if res[i][0] + res[j][0] - occs == m:
                    # return ' '.join(str(x) for x in sorted([res[i][1], res[j][1]]))
                    return "YES"
        return "NO"


def main():
    problem = Problem()
    problem.solve()


def __starting_point():
    main()


__starting_point()
