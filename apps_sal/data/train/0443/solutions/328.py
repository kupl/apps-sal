class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # return sum(1 for i in range(len(rating)) for j in range(i) for k in range(j) if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k])

        max_rating = 100000

        def strictly_monotonic(
            rating: List[int],
            previous_rating: int,
            remaining_ratings: int,
            ascending: bool,
        ) -> int:
            if not remaining_ratings:
                return 1
            if not rating:
                return 0
            if ascending ^ (rating[0] < previous_rating):
                return strictly_monotonic(
                    rating[1:], rating[0], remaining_ratings - 1, ascending
                ) + strictly_monotonic(
                    rating[1:], previous_rating, remaining_ratings, ascending
                )
            else:
                return strictly_monotonic(
                    rating[1:], previous_rating, remaining_ratings, ascending
                )

        return strictly_monotonic(rating, 0, 3, ascending=True) + strictly_monotonic(
            rating, max_rating + 1, 3, ascending=False
        )

