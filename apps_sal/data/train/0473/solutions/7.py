class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ arr[i]

        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                for k in range(j, n):
                    t = prefix[i - 1] if i > 0 else 0
                    if prefix[j - 1] ^ t == prefix[k] ^ prefix[j - 1]:
                        # print(i, j, k, prefix[i - 1], prefix[j - 1], prefix[k])
                        ans += 1
        return ans
