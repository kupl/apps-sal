class Solution:

    def numTeams(self, rating: List[int]) -> int:

        return self.increaser(rating, 0, 0) + self.decreaser(rating, 0, pow(10, 5) + 1)

    def increaser(self, rating, num, last):

        if num == 3:
            return 1

        if len(rating) == 0:
            return 0

        count = 0
        for i in range(len(rating)):

            if rating[i] > last:
                count += self.increaser(rating[i + 1:], num + 1, rating[i])

        return count

    def decreaser(self, rating, num, last):

        if num == 3:
            return 1

        if len(rating) == 0:
            return 0

        count = 0
        for i in range(len(rating)):

            if rating[i] < last:
                count += self.decreaser(rating[i + 1:], num + 1, rating[i])

        return count
