class Solution:
    def numTeams(self, rating: List[int]) -> int:

        ratings = [[]]

#         for items in rating:
#             ratings += [item + [items] for item in ratings if len(item) < 3]

#         count = 0
#         for item in ratings:
#             if len(item) == 3:
#                 if item[0] > item[1] and item[1] > item[2]:
#                     count += 1
#                 elif item[0] < item[1] and item[1] < item[2]:
#                     count += 1

        n = len(rating)

        count = 0
        for index_1 in range(0, n):
            for index_2 in range(index_1 + 1, n):
                for index_3 in range(index_2 + 1, n):
                    if rating[index_1] < rating[index_2] and rating[index_2] < rating[index_3]:
                        count += 1

        for index_1 in range(n - 1, -1, -1):
            for index_2 in range(index_1 - 1, -1, -1):
                for index_3 in range(index_2 - 1, -1, -1):
                    if rating[index_1] < rating[index_2] and rating[index_2] < rating[index_3]:
                        count += 1

        return count
