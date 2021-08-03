class Solution:
    def numTeams(self, rating: List[int]) -> int:
        greater = defaultdict(int)
        less = defaultdict(int)
        ans = 0

        for i in range(len(rating) - 1):
            for j in range(i + 1, len(rating)):
                if rating[j] > rating[i]:
                    greater[i] += 1
                else:
                    less[i] += 1
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating)):
                if rating[i] < rating[j]:
                    ans += greater[j]
                else:
                    ans += less[j]

        return ans
