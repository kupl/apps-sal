from queue import PriorityQueue
#[11, 111, 22,  222, 33,  333,44,444]


class Solution:
    def getminSum(self, jobDifficulty, d, memo, start, end):
        #print (d,start,end)
        if (start, end, d) in memo:
            return memo[(start, end, d)]
        if d == 1:
            return max(jobDifficulty[start:end + 1])
        if end - start + 1 == 1:
            return -1
        # one split
        minSum = -1
        for i in range(start + 1, end + 1):
            part1 = max(jobDifficulty[start:i])

            part2 = self.getminSum(jobDifficulty, d - 1, memo, i, end)
            if part2 == -1:
                continue
            if minSum == -1:
                minSum = part1 + part2
            else:
                minSum = min(minSum, part1 + part2)

        memo[(start, end, d)] = minSum
        #print(d, memo)
        return minSum

    def minDifficulty(self, jobDifficulty, d) -> int:

        memo = {}
        start = 0
        end = len(jobDifficulty) - 1
        result = self.getminSum(jobDifficulty, d, memo, start, end)
        print(memo)
        return result
