class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = collections.Counter()
        for i in arr:
            count[i % k] += 1
        for i in range(1, k // 2 + 1):
            if count[i] != count[k - i]:
                return False
            if count[0] % 2 != 0:
                return False
        return True
