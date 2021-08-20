class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) % 2 or sum(arr) % k:
            return False
        rems = [0] * k
        for a in arr:
            rems[a % k] += 1
        if rems[0] % 2:
            return False
        for i in range(1, k):
            if rems[i] != rems[k - i]:
                return False
        return True
