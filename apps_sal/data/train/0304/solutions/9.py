class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        age_dic = {age: ages.count(age) for age in range(1, 121)}
        pairs = 0
        for A in range(1, 121):
            for B in range(1, 121):
                if B <= 0.5 * A + 7:
                    continue
                elif B > A:
                    continue
                elif B > 100 and A < 100:
                    continue
                else:
                    pairs += age_dic[A] * age_dic[B]
                    if A == B:
                        pairs -= age_dic[A]
        return pairs
