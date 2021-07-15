from collections import defaultdict
from sys import stdin


class Solver:

    @staticmethod
    def build_dict(l):
        mp = defaultdict(int)
        for val in l:
            mp[val] = mp[val] + 1
        return mp

    @staticmethod
    def build_cnt_list(mp):
        lst = [v for (k, v) in list(mp.items())]
        return lst

    def __init__(self, l):
        self.__L = l

    @staticmethod
    def get_largest_power_of_2(n):
        # for p in reversed(range(31)):
        for p in range(30, -1, -1):
            if 1 << p <= n:
                return 1 << p
        return 1

    def solve(self):
        mp = Solver.build_dict(self.__L)
        cnt_lst = Solver.build_cnt_list(mp)
        cnt_lst.sort()
        cnt_lst.reverse()

        ans = cnt_lst[0]

        for start_cand in range(cnt_lst[0], 0, -1):
            if start_cand % 2 == 0 :
                ans2 = 0
                nxt = start_cand
                for cnt in cnt_lst:
                    if cnt >= nxt:
                        ans2 += nxt
                        if nxt % 2 != 0:
                            break
                        nxt //= 2
                    else:
                        break
                ans = max(ans, ans2)

        return ans


def main():
    n = int(stdin.readline())
    inp = list(map(int, stdin.readline().split()))

    # print(n)
    # print(inp)
    solver = Solver(inp)
    # print(Solver.build_dict(inp))
    print(solver.solve())


main()

