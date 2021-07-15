class Solution:
    def numTeams(self, rating: List[int]) -> int:
        return len(Solution.generate_teams(rating))
    
    @staticmethod
    def generate_teams(rating):
        teams = []
        rating_copy = rating
        negative_rating = [-num for num in rating]
        
        for rating in (rating_copy, negative_rating):
            for i in range(len(rating)):
                curr_first_soldier = rating[i]
                for j in range(i + 1, len(rating)):
                    curr_second_soldier = rating[j]
                    if i != j and curr_second_soldier > curr_first_soldier:
                        for k in range(j + 1, len(rating)):
                            curr_third_soldier = rating[k]
                            if k != j and curr_third_soldier > curr_second_soldier:
                                teams.append((curr_first_soldier, curr_second_soldier, curr_third_soldier))
        return teams
    
class SolutionTest:
    @staticmethod
    def test_generate_teams():
        test_ratings = [2, 3, 7, 1, 8, 9]
        
        actual_teams = [(2,3,7),(2,3,8),(2,3,9),(2,7,8),(2,7,9),(2,8,9),(3,7,8),(3,7,9),(3,8,9),(7,8,9),(1,8,9)]
        expected_teams = Solution.generate_teams(test_ratings)
        
        return actual_teams == expected_teams
    
print(SolutionTest.test_generate_teams())
