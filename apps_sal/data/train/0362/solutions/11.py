# Time: O(40 * 2^n * n), where n is the number of people, n <= 10
# Explain: There are total hat*assignedPeople = 40*2^n states in dfs(..hat, assignedPeople...) function, each state needs a loop up to n times (int p : h2p[hat]) to calculate the result.
# Space: O(40 * 2^n)

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        hat_to_ppl = [[] for _ in range(41)]
        for i, person in enumerate(hats):
            for hat_preference in person:
                hat_to_ppl[hat_preference].append(i)

        # Remove entries for unwanted hats
        hat_to_ppl = list([x for x in hat_to_ppl if x])

        num_hats = len(hat_to_ppl)
        num_ppl = len(hats)

        if num_hats < num_ppl:
            return 0

        @functools.lru_cache(None)
        def dp(i, mask):
            # Mask signifies person state
            if i == num_hats:
                if bin(mask).count('1') == num_ppl:
                    return 1
                else:
                    return 0

            # Not using current hat
            res = dp(i + 1, mask)

            for person in hat_to_ppl[i]:
                # Person is not wearing a hat already
                if (mask & (1 << person)) == 0:
                    mask |= 1 << person
                    res += dp(i + 1, mask)
                    mask ^= 1 << person

            return res % (10**9 + 7)

        return dp(0, 0)
