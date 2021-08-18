class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans, size = 0, len(arr)
        xor = [0] * size
        xor[0] = arr[0]
        for i in range(1, size):
            xor[i] = arr[i] ^ xor[i - 1]

        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j, size):
                    a = xor[j - 1] ^ xor[i - 1] if i > 0 else xor[j - 1]
                    b = xor[k] ^ xor[j - 1]
                    if a == b:
                        ans += 1
        return ans
