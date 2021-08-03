class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counts = Counter(ages)
        requests = 0

        conditions = [
            lambda ageA, ageB: 0.5 * ageA + 7 >= ageB,
            lambda ageA, ageB: ageA < ageB
        ]

        def canSendRequest(ageA, ageB):
            # if any condition is True, then we can't request friend
            return not any(condition(ageA, ageB) for condition in conditions)

        for ageA, countA in counts.items():
            for ageB, countB in counts.items():
                if canSendRequest(ageA, ageB):

                    if ageA == ageB:
                        requests += countA * (countA - 1)
                    else:
                        requests += countA * countB

        return requests
