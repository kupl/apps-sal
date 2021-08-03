class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        a = sorted(ages)
        i, j, k = 0, 0, 0
        ans = 0
        for i in range(1, len(a)):
            if a[i] <= 14:
                continue
            lb = a[i] * 0.5 + 7
            while a[j] <= lb:
                j += 1
            ans += i - j
            if a[k] != a[i]:
                k = i
            ans += i - k
        return ans
