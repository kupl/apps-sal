class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # Note age[B] > 100 && age[A] < 100 is redundant since we have age[B] > age[A]
        def wantToRequest(A, B):
            return not(B <= 0.5 * A + 7 or B > A)

        count = Counter(ages)
        ans = 0
        ages = [*sorted(count.keys())]

        for i, a in enumerate(ages):
            for j in range(0, i + 1):
                b = ages[j]
                if wantToRequest(a, b):
                    ans += count[a] * count[b] if a != b else count[a] * (count[b] - 1)

        return ans
