class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return 0
        xors = [i for i in arr]
        for i in range(1, len(xors)):
            xors[i] ^= xors[i - 1]
        ans = 0
        for j in range(1, len(xors)):
            cnt = Counter([xors[j - 1] ^ xors[i - 1] for i in range(1, j)])
            cnt[xors[j - 1]] = cnt.get(xors[j - 1], 0) + 1
            for k in range(j, len(xors)):
                ans += cnt.get(xors[k] ^ xors[j - 1], 0)
        return ans
