class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counts = Counter(ages)
        requests = 0

        conditions = [
            lambda ageA, ageB: 0.5 * ageA + 7 >= ageB,
            lambda ageA, ageB: ageA < ageB
        ]

        def canRequestFriend(ageA, ageB):
            return not any(condition(ageA, ageB) for condition in conditions)

        for ageA, countA in list(counts.items()):
            for ageB, countB in list(counts.items()):
                if canRequestFriend(ageA, ageB):
                    if ageA == ageB:
                        requests += countA * (countA - 1)
                    else:
                        requests += countA * countB

        return requests
