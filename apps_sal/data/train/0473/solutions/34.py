class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        d = defaultdict(list)
        d[0].append(-1)
        cur, rst = 0, 0
        for i, a in enumerate(arr):
            cur ^= a
            if i > 0:
                for j in d[cur]:
                    rst += i-j-1
            d[cur].append(i)
        return rst
