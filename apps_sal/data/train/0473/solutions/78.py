class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] ^ arr[i]
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                for k in range(j, n):
                    if ps[i] ^ ps[j] == ps[j] ^ ps[k + 1]:
                        res += 1
        return res
