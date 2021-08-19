class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        count = collections.Counter(ages)
        ans = 0
        for (A, countA) in count.items():
            for (B, countB) in count.items():
                if B <= 0.5 * A + 7:
                    continue
                elif B > A:
                    continue
                elif B > 100 and A < 100:
                    continue
                ans += countA * countB
                if A == B:
                    ans -= countA
        return ans
