class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freqs = [0] * k
        for n in arr:
            freqs[n % k] += 1
        for r in range(1, k // 2 + k % 2):
            if freqs[r] != freqs[k - r]:
                return False
        return not freqs[0] % 2
