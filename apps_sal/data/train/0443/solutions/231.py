class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        team_cand_a = [[] for _ in range(n)]
        a_count = 0
        team_cand_d = [[] for _ in range(n)]
        d_count = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    team_cand_a[i].append([i, j])
                elif rating[j] < rating[i]:
                    team_cand_d[i].append([i, j])
        print(team_cand_a)
        print(team_cand_d)
        for ca in team_cand_a:
            for ij in ca:
                a_count += len(team_cand_a[ij[-1]])
        for cd in team_cand_d:
            for ij in cd:
                d_count += len(team_cand_d[ij[-1]])

        return a_count + d_count
