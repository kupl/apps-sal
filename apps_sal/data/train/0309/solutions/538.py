'''

[9,4,7,2,10]

0, 



[3,6,9,12]

0 -> 1

3 -> 2

3 -> 3

6 -> 1



'''


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        if not A:
            return 0

        if len(A) == 1:
            return 1

        diff_map = {}

        for it1 in range(1, len(A)):

            num1 = A[it1]

            for it2 in range(it1):

                num2 = A[it2]

                diff = num1 - num2

                if (it2, diff) not in diff_map:
                    diff_map[(it2, diff)] = 1

                diff_map[(it1, diff)] = diff_map[(it2, diff)] + 1

        return max(diff_map.values())
