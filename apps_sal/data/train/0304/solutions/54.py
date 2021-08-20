from collections import Counter


class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        c = Counter(ages)
        return sum((self.can_be_friend(a, b) * c[a] * (c[b] - (a == b)) for a in c for b in c))

    def can_be_friend(self, age1, age2):
        if age2 <= 0.5 * age1 + 7 or age2 > age1 or (age2 > 100 and age1 < 100):
            return False
        return True
