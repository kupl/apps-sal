from collections import Counter


class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:

        def is_valid(a, b):
            return not any([b <= 0.5 * a + 7, b > a, b > 100 and a < 100])
        counts = Counter(ages)
        ages = list(counts)
        requests = 0
        for i in range(len(ages)):
            for j in range(len(ages)):
                count = counts[ages[i]] * (counts[ages[i]] - 1) if i == j else counts[ages[i]] * counts[ages[j]]
                requests += int(is_valid(ages[i], ages[j])) * count
        return requests
