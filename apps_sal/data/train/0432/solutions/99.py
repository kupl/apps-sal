class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        l = nums[:]
        l.sort()
        n = len(l)
        d = Counter(l)
        count = 0
        for i in range(n):
            if d[l[i]] != 0:
                d[l[i]] -= 1
                f = 0
                for j in range(l[i] + 1, l[i] + k):
                    if d[j] == 0:
                        f = 1
                        break
                    d[j] -= 1
                if f == 1:
                    return False
        return True
