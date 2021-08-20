class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        if n & 1:
            return False
        bucket = [0] * k
        for a in arr:
            bucket[(k + a % k) % k] += 1
        if bucket[0] % 2:
            return False
        for i in range(1, k):
            if bucket[i] != bucket[k - i]:
                return False
        return True
