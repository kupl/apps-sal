class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:

        def helper(hat, assignedPeople):
            if assignedPeople == target_state:
                return 1

            if hat > 40:
                return 0

            if dp[hat][assignedPeople] is not None:
                return dp[hat][assignedPeople]

            res = 0
            res += helper(hat + 1, assignedPeople)

            for person in hat2person[hat]:
                if assignedPeople & (1 << person) != 0:
                    continue
                res += helper(hat + 1, assignedPeople | (1 << person))

            dp[hat][assignedPeople] = res
            return dp[hat][assignedPeople]

        n = len(hats)
        M = 10**9 + 7
        hat2person = [[] for _ in range(41)]
        for i in range(n):
            for hat in hats[i]:
                hat2person[hat].append(i)
        target_state = (1 << n) - 1
        dp = [[None for j in range((1 << n))] for i in range(41)]

        return helper(1, 0) % M
