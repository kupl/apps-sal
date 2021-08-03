class Solution:
    def minOperations(self, n: int) -> int:
        avg = n

        count = 0
        # print(\"n = {}\".format(n))
        for i in range((n // 2)):
            count += avg - (2 * i + 1)
            # print(\"i = {}, count = {}\".format(i, count))

        return count
