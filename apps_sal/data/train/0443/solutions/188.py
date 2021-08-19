class Solution:

    def numTeams(self, rating: List[int]) -> int:
        a = rating
        n = len(a)
        ans = 0
        for i in range(n):
            left = [0, 0]
            for j in range(i):
                if a[j] < a[i]:
                    left[0] += 1
                elif a[j] > a[i]:
                    left[1] += 1
            right = [0, 0]
            for j in range(i + 1, n):
                if a[j] < a[i]:
                    right[0] += 1
                elif a[j] > a[i]:
                    right[1] += 1
            ans += left[0] * right[1] + left[1] * right[0]
        return ans
