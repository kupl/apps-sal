class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_library = {}

        for age in ages:
            age_library[age] = age_library.get(age, 0) + 1

        res = 0
        for A, numA in list(age_library.items()):
            for B, numB in list(age_library.items()):
                if not (B <= 0.5 * A + 7 or B > A or (B > 100 and A < 100)):
                    res += numA * numB - numA * (A == B)
        return res
