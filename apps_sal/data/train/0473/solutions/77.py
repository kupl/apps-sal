class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_xor = [0] + arr
        for i in range(1, n + 1):
            prefix_xor[i] = prefix_xor[i] ^ prefix_xor[i - 1]
        res = 0
        for i in range(n - 1):
            for k in range(i + 1, n):
                for j in range(i + 1, k + 1):
                    if prefix_xor[k + 1] ^ prefix_xor[j] == prefix_xor[j] ^ prefix_xor[i]:
                        res += 1
        return res
