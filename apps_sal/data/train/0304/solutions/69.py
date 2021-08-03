class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_dict = collections.Counter(ages)
        sorted_ages = sorted(age_dict.keys())
        requests = 0
        for i in sorted_ages:
            for j in sorted_ages:
                if (j > 100 and i < 100) or (j <= 0.5 * i + 7):
                    continue
                if j > i:
                    break
                if i == j:
                    requests += age_dict[i] * (age_dict[j] - 1)
                else:
                    requests += age_dict[i] * age_dict[j]
        return requests
