class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # worst case is iterate from i -> j -> k and k -> arr.length and test out each comb
        # compute i -> j - 1, keep counter for each i, j comb
        # compute j -> k
        # for each i -> j,
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
