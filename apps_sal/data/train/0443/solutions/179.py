class Solution:
    def numTeams(self, rating: List[int]) -> int:
        table = [[1 if rating[i] > rating[j] else 0 for j in range(i + 1, len(rating))] for i in range(0, len(rating) - 1)]
        table = table + [[]]
        count = 0

        for i in range(0, len(table)):
            for j in range(0, len(table[i])):
                if table[i][j] == 1:
                    count += sum(table[i + 1 + j])
                else:
                    count += (len(table[i + 1 + j]) - sum(table[i + 1 + j]))

        return count
