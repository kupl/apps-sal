class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        # Question: list is arithmetic with constant diff bet elements
        # dict of dict -> for each index key have dict with diff as key and count as value
        cur = collections.defaultdict(dict)

        maxSeq = 0

        # this is DP problem but this is one way to solve without DP, by storing all
        for i, v in enumerate(A):
            for j in range(i):
                val = v - A[j]    # end -start
                # diff cnt + previous diff cnt from start(j)
                cur[i][val] = 1 + cur[j].get(val, 1)  # def is 1 and not 0 since first time its 2 no's diff
                # print(cur)
                if maxSeq < cur[i][val]:
                    maxSeq = cur[i][val]

        return maxSeq
        # return max(cur[i][j] for i in cur for j in cur[i])

# [3,6,9,12]
# defaultdict(<class 'dict'>, {})
# defaultdict(<class 'dict'>, {0: {}, 1: {3: 2}})
# defaultdict(<class 'dict'>, {0: {}, 1: {3: 2}, 2: {6: 2}})
# defaultdict(<class 'dict'>, {0: {}, 1: {3: 2}, 2: {6: 2, 3: 3}})
# defaultdict(<class 'dict'>, {0: {}, 1: {3: 2}, 2: {6: 2, 3: 3}, 3: {9: 2}})
# defaultdict(<class 'dict'>, {0: {}, 1: {3: 2}, 2: {6: 2, 3: 3}, 3: {9: 2, 6: 2}})
# defaultdict(<class 'dict'>, {0: {}, 1: {3: 2}, 2: {6: 2, 3: 3}, 3: {9: 2, 6: 2, 3: 4}})
