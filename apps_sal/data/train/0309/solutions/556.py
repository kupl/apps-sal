class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        a = A
        n = len(a)

        count = [{} for i in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = a[i] - a[j]

                if diff in count[j]:
                    count[i][diff] = 1 + count[j][diff]
                else:
                    count[i][diff] = 1

        max_val = 0
        for item in count:
            if item:
                max_val = max(max_val, max(item.values()))

        return max_val + 1
