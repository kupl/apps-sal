class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        prefix = list(arr)
        for i in range(1, n):
            prefix[i] ^= prefix[i - 1]
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    a = prefix[j - 1] ^ prefix[i] ^ arr[i]
                    b = prefix[k] ^ prefix[j - 1]
                    ans += 1 if a == b else 0
        return ans
