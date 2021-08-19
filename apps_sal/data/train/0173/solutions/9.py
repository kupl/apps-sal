class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        m = {i: 0 for i in range(k)}
        for a in arr:
            m[a % k] += 1
        for i in range(k):
            if i == 0:
                if m[i] % 2 != 0:
                    return False
            elif m[i] != m[k - i]:
                return False
        return True
