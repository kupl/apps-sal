class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        d = {}
        d[0] = 1

        sm = 0
        even = 0
        for i in range(n):
            sm += arr[i]
            sm %= 2
            if sm < 0:
                sm += 2
            if sm in d:
                even += d[sm]
            if sm not in d:
                d[sm] = 0
            d[sm] += 1

        return (n * (n + 1) // 2 - even) % (10**9 + 7)
