class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        cumxor = [arr[0]]
        for i in range(1, n):
            cumxor.append(cumxor[i - 1] ^ arr[i])
        cumxor.append(0)
        res = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                if cumxor[i - 1] == cumxor[j]:
                    res += j - i
        return res
