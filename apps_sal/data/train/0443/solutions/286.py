class Solution:
    def numTeams(self, ratings: List[int]) -> int:
        # maintain a data structure where dict[index] stores another dict keyed by ranking (r) \\
        # and stores number of rankings greater than that ranking in the rating list
        res = 0

        numRatings = len(ratings)
        sortedRatings = sorted(ratings)

        mapping = dict()
        mapping_rev = dict()
        mapping[len(ratings)] = dict(list(zip(ratings, [0] * numRatings)))
        mapping_rev[len(ratings)] = dict(list(zip(ratings, [0] * numRatings)))
        for index, rating in list(enumerate(ratings))[::-1]:
            mapping[index] = dict()
            mapping_rev[index] = dict()
            for tmpRating in ratings:
                if tmpRating < rating:
                    mapping[index][tmpRating] = mapping[index + 1][tmpRating] + 1
                    mapping_rev[index][tmpRating] = mapping_rev[index + 1][tmpRating]
                else:
                    mapping[index][tmpRating] = mapping[index + 1][tmpRating]
                    mapping_rev[index][tmpRating] = mapping_rev[index + 1][tmpRating] + 1

        for i, rating_i in list(enumerate(ratings)):
            # check triplets starting with rating[i]
            for j, rating_j in list(dict(list(zip(list(range(i + 1, numRatings + 1)), ratings[i + 1:]))).items()):
                if rating_j > rating_i:
                    res += mapping[j + 1][rating_j]
                else:
                    res += mapping_rev[j + 1][rating_j]

        return res
