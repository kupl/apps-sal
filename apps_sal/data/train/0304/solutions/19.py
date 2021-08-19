class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:

        def req(A, B):
            if B <= 0.5 * A + 7 or B > A or (B > 100 and A < 100):
                return False
            return True
        cnt = Counter(ages)
        ans = 0
        for i in cnt:
            if cnt[i] > 1 and req(i, i):
                ans += cnt[i] * (cnt[i] - 1)
            for j in cnt:
                if i != j and req(i, j):
                    ans += cnt[i] * cnt[j]
        return ans
