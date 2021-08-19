class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        # https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/discuss/608778/Java-Top-down-DP-%2B-Bitmask-Clean-code
        # hat: current hat; assignedPeople: bitmask for n people (0: this person has not been assigned a hat, 1 otherwise)

        def helper(hat, assignedPeople):
            if assignedPeople == target_state:
                return 1

            if hat > 40:  # no remaining hat
                return 0

            if dp[hat][assignedPeople] is not None:
                return dp[hat][assignedPeople]

            res = 0
            # case 1: do not use current hat
            res += helper(hat + 1, assignedPeople)

            # case 2: use current hat
            # check every possible person that is allowed to wear the current hat
            for person in hat2person[hat]:
                # if person has a hat already
                if assignedPeople & (1 << person) != 0:
                    continue
                res += helper(hat + 1, assignedPeople | (1 << person))

            dp[hat][assignedPeople] = res
            return dp[hat][assignedPeople]

        n = len(hats)
        M = 10**9 + 7
        # h2p[i] indicates the list of people who can wear i_th hat
        hat2person = [[] for _ in range(41)]
        for i in range(n):
            for hat in hats[i]:
                hat2person[hat].append(i)
        # print(hat2person)
        target_state = (1 << n) - 1  # all people have weared a hat
        dp = [[None for j in range((1 << n))] for i in range(41)]

        return helper(1, 0) % M
