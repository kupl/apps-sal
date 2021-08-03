class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        sum = 0
        counts = collections.Counter(ages)
        ages = sorted(counts.keys())
        for A in range(0, len(ages)):
            for B in range(0, len(ages)):
                condition1 = ages[B] <= 0.5 * ages[A] + 7
                condition2 = ages[B] > ages[A]
                condition3 = ages[B] > 100 and ages[A] < 100
                if not (condition1 or condition2 or condition3):
                    if A != B:
                        sum += counts[ages[A]] * counts[ages[B]]
                    else:
                        sum += (counts[ages[A]] - 1) * counts[ages[B]]
        return sum
