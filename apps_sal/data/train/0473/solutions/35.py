class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(1, n):
            l = Counter()
            a = 0
            for j in range(i - 1, -1, -1):
                a ^= arr[j]
                l[a] += 1
            a = 0
            for j in range(i, n):
                a ^= arr[j]
                ans += l[a]
        return ans
