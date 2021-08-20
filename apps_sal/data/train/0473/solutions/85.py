class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        cum = [0]
        for n in arr:
            cum.append(cum[-1] ^ n)
        ans = 0
        for i in range(0, len(arr) - 1):
            for k in range(i + 1, len(arr)):
                for j in range(i + 1, k + 1):
                    if cum[i] ^ cum[j] == cum[k + 1] ^ cum[j]:
                        ans += 1
        return ans
