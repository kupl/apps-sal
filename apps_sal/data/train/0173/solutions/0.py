class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k
        for n in arr:
            freq[n % k] += 1
        if freq[0] % 2:
            return False
        for i in range(1, k // 2 + 1):
            if freq[i] != freq[k - i]:
                return False
        if k % 2 is 0:
            if freq[k // 2] % 2:
                return False
        return True
