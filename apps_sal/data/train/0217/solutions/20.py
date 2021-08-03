class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:

        # my solution ... 760 ms ... 98 % ... 40.6 MB ... 15 %
        #  time: O(nlogn)
        # space: O(logn)

        res = set()
        tot = set()
        for a in A:
            res = {prev | a for prev in res} | {a}  # 得出以当前 a 结尾的 subarray
            tot |= res                              # 把结果并入 tot
        return len(tot)
