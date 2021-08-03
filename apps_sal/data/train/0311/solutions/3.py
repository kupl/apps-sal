class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        result = [1] * n

        for i in range(n - 1):
            if ratings[i + 1] > ratings[i]:
                result[i + 1] = result[i] + 1

        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                result[i - 1] = max(result[i] + 1, result[i - 1])

        return sum(result)
