class Solution:
    def isPossibleDivide(self, nums, k):
        d = collections.Counter(nums)
        roots = [n for n in d if not d[n - 1]]
        for r in roots:
            for i in reversed(range(r, r + k)):
                if d[i] < d[r]:
                    return False
                d[i] -= d[r]
                if not d[i] and d[i + 1]:
                    roots.append(i + 1)
        return True
