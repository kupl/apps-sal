def fun(x):
    cnt = 0
    while x != 1:
        x = x / 2 if x % 2 == 0 else 3 * x + 1
        cnt += 1
    return cnt


class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        lst = sorted([(x, fun(x)) for x in range(lo, hi + 1)], key=lambda x: (x[1], x[0]))
        print(lst, k)
        return lst[k - 1][0]
